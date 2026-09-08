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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 08:58:33</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6x5uhk61jmBjpHnFvJaGTmx5ZYJRNf8lu2Z1I-JdraKkF0ebA1wx4Dng5WTzl4-PFo1ecWsxepGFa0-xAVusjbaLQ0xrBkRjD49kfl8d4VhJC6VM6SNAvzqLCAb-HzTv0EPDHpLV_lykigIu9adANoZqfoLwH-xCiLLPBn2d4kAfI4444nJQlTl_WZGm0JoDvZCZaeq94rilOM91izsiqWizBQmL3boHrOkRaQI3-BbI5zLarF3bXkpR7JPGYjEW72zj51MMxjuUIPPsVjb7h9_Qn9sMw-fmpsZGtTLo3OF6FSCDvlCrCKLG_objQKiok7LbTsfNDDEvQN2GsKiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpLoRmWsNBY-DCxpFKzRJKWrGgDaFx_Wl8wApnELlzjtHho24X_zUkYcYmDJrHlol0WG_4mv9qPRQ2aPZYj48mPK0_8rDECL9azB6EJRYNpBRMr_0rQrYoaxGCi32SDgRzGaDRHzjybM39qxulTQx8vkAm6gknv5RqcYJBQLj6Yyl6S8TIdLAK9k6_BbyEf4YBlhT5QtB7KJeZpGYXKUEragMhH7ch-mwye5RDJFwsBqUUDc0UROnLkTBTyi7bNu1-sum0BJgcGh14lVBafjOLPQvas-4Zw5Ptan7RuyOE1psUGx-Vpx5N82KLT45Yi1K_GAAcTvjYoPWO6ymaF6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4xkZvDe_TRochKG9OElTNQ5FAOZmPVCju0xMPY-N94c-UFq4HoE8LgngXeU_YDXVu01NzSHQEwHHaU-AoLT74htlRTVs2SHjeMHcBdS9DePygfhIAvKB0CBuZm5JJbqhxNd5ras9zBrC96cKDy5Aqs5wrXV2x0n9MEgY2vjcbQibhAoyxDJp0xkR_4JV4GRcw6suy1uCwS3ASKZLNrPNHAy-Vb5WbaBCml85UQbxY2e5tABQbEKg_nMSqPiBRFFss4YAZ56EK4CXp3Rx4EoPg137Cg9VNndQh-K_yWdBIclcfKZuUFmZHL_dLj3m3zuRumHI5lbjeZGBCpEfPaBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAWSv0TbJVAS3ZbPhjDzTqgCYna6_5OpObGhDB80OXhfKOn7LVisyvQl3SPYmnT3J93mZ0naMgAuVSTfuG1pGPu6IZNLJ4e9ZJaPT1X6O4oqJySmaSZaQOeQkn84mvS-h32g27EKvRkVQNit7HUS8BHZpAJNmoSaRdI8zANz9WZwV3qdeTClRVy7C-zs0HqvF_HS83PcHHJcwKxgGk33KHKAlXNc-4N7AABJk4FM6n0m_fIATVTybFRABkqAX7XA3nG_6bMc7ySRAgbSgGhAmJFppfd3nLHCYXuswVthwfh51kHaWnYDJmudHWS0_FfAYU4Qqh3aKf2opeOsubW78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=aqd-fZkeH8subkV_eqN0Ikgu4wuIZIB1ZWKxEkmgpWr50El5Rwq_-moT6j8PaIIwiU4fSfJzFdDGy19kOJd7YzxWK9DzOJG4Wse7GxOGmZEKyfy1Ne9ZchGDl6sMBNF4usIOsDezDWWoD7cX-2IhF-J07lQA1B1Nl59th68SMABm5OYsJIhCYmLKpt5cJsmhNzcLP901mQPqoilBal4dIiicamnHWwXWooCY3efUtiN6EM-7j5Sn7igJ1KhYxHtTh6stLt2d4FqYGBgZfxjWYUyg_ddZOwuSkJ4UpqhyG8XoEiVWG5ae38iRYm835FrxB6n51kliAapz5P6I0QwrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=aqd-fZkeH8subkV_eqN0Ikgu4wuIZIB1ZWKxEkmgpWr50El5Rwq_-moT6j8PaIIwiU4fSfJzFdDGy19kOJd7YzxWK9DzOJG4Wse7GxOGmZEKyfy1Ne9ZchGDl6sMBNF4usIOsDezDWWoD7cX-2IhF-J07lQA1B1Nl59th68SMABm5OYsJIhCYmLKpt5cJsmhNzcLP901mQPqoilBal4dIiicamnHWwXWooCY3efUtiN6EM-7j5Sn7igJ1KhYxHtTh6stLt2d4FqYGBgZfxjWYUyg_ddZOwuSkJ4UpqhyG8XoEiVWG5ae38iRYm835FrxB6n51kliAapz5P6I0QwrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImLuEprB2TGbAXhqoGFe2rw8LU8R5Vqqby8ErhsP836SpbxLa9wid_v96Rrg3VoQ-agP9dQXfpNCugRfrjzTWQZSH5PFceMt4WG6CauiW3pSI3CmOSfVl3SyqZxjI7Iyt7oYAc_vX06JrSwjTssLcVwvM_O0As0O3z6DWIYUj66Vv4a28VJdKUpl_hPHlv-akAanv5UxrtCgnvTpC-ywabM-3VqHCtrw7tLD7Ypu162VQ0zKGod6b-DL-DZFrrseGHVj0mWIIUmI5NC6Db-Kii-ec9ea0mDbei8CPlfDGw-T2I29AKNr76Vh20CC0pNXrPLLFs3gW_txf05rIlFwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuSKgSI85PxtuAaLMOT2Q7B8tECqwxwPLJGrDsELPw_B45LeImWI1nOltmJc_7pHgEUWARtM9y4XDMRXJOwv1Je0IASP7nrvUjXRB9BoiQaXAhBFOgztnpNCyGyfUVvlujMki5ImUA3rO7dgaEMyoXRpm7qSHXUDYZKYlPfV3XG9WsYj5Uk1DoWgs_o8ISz7X_3C30u2dcqu67h9DvGShnHmWrehLr0ELOSy2wKgNhcCFvoE9Nh017sKjYYDqos24GFJ9jm3SCKOkr__eIMh5-Ze09DFbfvX3IEqv22WKfa4VYYrMkammWP1UBqBoZGF0Vr7oxs6UTx2kUL2nYjJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9V2ltq-Tpam9MsOx1D_VFCQn07mfX0ejLw0Bvjo_q8XBI0N258r6ZbY1LsYGdGCzfljj6qSAjvCUk8-SE6Y6CN6nKm7M3LkIemLrkyv9vqIEhiT5RVrhtWLcj35lZzhAh6S2FiKmELAOWuayeuQdnH-x19dMOU3CG3IM_qlk2NJfpwZ4_p0SJf9MWUTIq9SsfXvksOgULvBzkw7LDD7dq2KGwrZvEXpP7LvLn_sfs-vsjtTpPyGi-wIpeT6vUInLTmDlXXY5SONqiUIRahHZGqQfpcoiijN6o5uAKbn_89G8LRNcjhXT0JBduRhSVUxoPAJnaGpFPLkDntBU7un6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOOED2ofN17j7GG0Y1wQjaGnnbi3ud2d8wZ9o4X4e1vw03RWz62sFoBea4kF1a8Do9YxYCUzUP_IAf0-fyc3x7cnoyBSbkn7muHh5087ifMPON2n8amDS9PSQmo8MPF4C8YJyW8nhC4uX9j49OlpDsovOAWbY3XiIQN4AEwPo9vVc9MN_15hcXISpshpZF7Tt_yQn4EO8x7I4-y4l2mtQrk4k9yJVijeTEVZ0M8crJq-E7HksqHCeuUIOl-P2e8M0_t5G9RagflVMaUT5hnVNm5v7IIO7F2CacTaiYLJJv53RsZtwKH2KvNtS1dXOUDOc3Ptthg_o85CP5nx4ElulA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMkV45XxAimGdsE-9bLJoP0CqSRvMME3B9Ffl_yDt58fTr0WPVkU7zVAzJtWfCrijlELB2Tfm4r45KJ7EwOJ6w1E9uqohwHsXyEEQfIC2PjhQml6RT4S9DIJ0OT-_bYV7NQYqVwYQACKuHuArVhVC1k6r0PK9gHHqTcy_pb9KSoCkJoxPtpCK2wh1esO97fxaULRYVqidyIzaCfoYKyZcYtFfRlYH6QAo1Sfxk3z59kEWUKEBb8dywNuP09DGAVcI5l5mv32xTE17oditUqSv8EzerWo4FGWoE_eDTqe6CKhY86pliDxivtQrq8R5fdGANdsSDcn0KHnrhVLkPBwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBjNFWUsn06uQB5VwbLID_MC-e0aOzCVseo1zUfZjKXJ2gjTNOAylWmdsA5ObnczjkwYwKUKeeI9gDgkiZwzCCzLjTbLwQtVX-dPzcGzU-P2Iekrm0sdjAvPaqy8GOY2oIPoCAxGNXJBAWhiZo0Aq3M8-w0scPw9uCwJUIEgZFbJfifKf_AT_zZE3adP14VBH8rRFTRZe2UkfV5FhxDQwvyaTGyyD3PTMlwuMf8Q_B1Oxr4aqANrznS1-xSPhKXlRnpY4yYobUYTN4_a-LRqrkf4-HsgI2slYAN2QkK_etm5UFuJyhudMV5xwPZ2K8VAMcHZ4IIS24KQVrF_1pzZAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnIu7z3XZ2cJXBv6AfZoQJDg136_MXmAQNomwVtZyUJI1qj5guJUfQsUOjfZxXCWqHmPAlxbHdbv7ADOyC7xmujQYHqLAjogfAXTUNu4ODoI51oQ4f6bYCXXslCzftgFesaAaRrIRCnTAZG6eZ0Rd6cKbDGS2nJ4QxRJMeUHtiXpiWaxPriau8VQYSJrN-m0rfQpJai0FXzrsz6cjeNIZyyd19uKx9a5nNTU4NoNOp3SLhl54ACYnF5kTzkfWhJajJI5lHLel1we38QRCeCQMcbRoyBV5dTzLkm5q26vFeIJmmvJX1DOTQSu_CnIVYRelea9KVt4UK56Ur4SqEHy1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nL13pNX_o7F1nyi13_Slj4Wkj1AnvGR5G6uFnLTysfEb0PnpjBKSEuSV8K3GThyvqTBqrE0pQdVpMmTz30ckp5oKnB_iunRyxQsB-4fPdav5z7XilRSW6FsHhpTckNQxJIg-j7WTdPGtORvXsIhjyZKNQZGuLBmoMwyUg5sb9Gjo1tx-LGeQxmVjmpYtek480eFZ1KICJkFFVBQnK7tq4ZKEhCl4P9KPRjCZN3pD59KSSE7qRvv4rKO-f4RZ3_YgCXq_CyPvdv2e0KQ9AvxH4MVgDTaY8cxpnZ1Ih09W_GUhQjgMZ03n7t4Os4ZoqGsxHyfGKxQjSqomSitmbSFqFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_JJhShVs7xsq5Uf7P9RWBa-sJwls4vkdQM1eaxRuR00OHatIQgEMeK3f-9WMgcay0Ivr7ScAC4aqL6OZtLDfu-Gp4RNbKRT7QeFclxX4l9EqbEl4OUO5MtFidEt1lYEie2JsHQO1BjlzPEUS80J0NAe6sgljNTfOSPQIv-Z_nV_Gd-XIWNHEXjMZIi7ZmqAJUlv-IepIxBnVTzPoFaI9E-OXHWsM-PsfUNoGw2wYJj_bjXEko_ANaYk4ON4HdHc34e78DFG8XKQ9SlqGG66EFbls60aceOG0uZ-SNKHeimTf7tvdgJEW-sCreLUEbMli-iDx3RmLIAp-tYhKIx5cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd76uhKMN1lCPOmxO1t9IbPZYL8FixSJ8aip2nBm6Vzs80NUZgDbmxYGSLOFNXl9SPmIadwTR4Bl_1y5iT_jEMriOsBfXHl33QMJoSJHL0gtD1ioiiG2GFZlBcNdTPyT47GEJb2F3wLFHb2BnVQe-djZlDd5y42U7SuLrZNH2idA6j_5J1UzbG4u661I5mPk1DzKtlb6ZB3ivyNBTx2Ys8S8mTp5xOAE0l7uFShWRcwDN16AfF9Ws4yUDP76BEOBAHPmV4ukL089ALrCpYogFVm6lBJlQZcYabSaiEWObrnA2Do8CRVB0GtH7ffnogvfu_OgFUREMaAVAXKFbxWyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=rws_o6TSWH9IiChcTwxwGYTxSrqfN0ncyr7EVo2SYJBCb44hF3ugbPHdn7HZYb92gt1xXgNQNKOGKnq999ElDRGHyzthLIczZq3UZ_sOhHgofeCEX_7HHWKsc406ZCBxD10av1aWyvtQjqs8vSiH0jskNpuI0uhananJhOKoiuhUaQp-MU5ac-s9IHwsu90FYTdZJnOW2gIgUM2oOLsWZnQy1CUOtRmVP3Y7kkYhTTi34Lh0x3u46dNdX_mptdwTuBxVO_Hu3bWS75Q_vNn7SjuHRxaPJ13JknuAE1hdWssiLwZff5DJSw-qqMxxiUX32fwgAAB5T0tOaCn7sVtpKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=rws_o6TSWH9IiChcTwxwGYTxSrqfN0ncyr7EVo2SYJBCb44hF3ugbPHdn7HZYb92gt1xXgNQNKOGKnq999ElDRGHyzthLIczZq3UZ_sOhHgofeCEX_7HHWKsc406ZCBxD10av1aWyvtQjqs8vSiH0jskNpuI0uhananJhOKoiuhUaQp-MU5ac-s9IHwsu90FYTdZJnOW2gIgUM2oOLsWZnQy1CUOtRmVP3Y7kkYhTTi34Lh0x3u46dNdX_mptdwTuBxVO_Hu3bWS75Q_vNn7SjuHRxaPJ13JknuAE1hdWssiLwZff5DJSw-qqMxxiUX32fwgAAB5T0tOaCn7sVtpKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=ghnFrrrncAPXPIgNEd63xj8zJG-uzNrhwdwA1mu4WKReXMcx3DQtmBEKl05wOQTWaEuvkoEXgUZA_GnaeYg3Ilsbzzm5qUiJ2ohXelY2ObX1j-XXUAeRWdw8Cv9FYYlU5EHl_muX_aJUCvXxFvWwfdmi-AC8DMcI1tSbKlLlKG2dl-VZvzPoY9F3UfEsVylwXST0TbQ9x8qDuxQHMYFbicZRYqkRXKX9AgoPilLMQDPR5H7BWVCUgSN8uq3cnMepC_61nYQZbT1inck4BkNfgLnMbGSRz50kk58NHQrN6Qh29sp8nUHTJAOkaSEU56DWCZraEOkBj6UiAkpNW0n8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=ghnFrrrncAPXPIgNEd63xj8zJG-uzNrhwdwA1mu4WKReXMcx3DQtmBEKl05wOQTWaEuvkoEXgUZA_GnaeYg3Ilsbzzm5qUiJ2ohXelY2ObX1j-XXUAeRWdw8Cv9FYYlU5EHl_muX_aJUCvXxFvWwfdmi-AC8DMcI1tSbKlLlKG2dl-VZvzPoY9F3UfEsVylwXST0TbQ9x8qDuxQHMYFbicZRYqkRXKX9AgoPilLMQDPR5H7BWVCUgSN8uq3cnMepC_61nYQZbT1inck4BkNfgLnMbGSRz50kk58NHQrN6Qh29sp8nUHTJAOkaSEU56DWCZraEOkBj6UiAkpNW0n8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsd1QQk79bmbZStt6u1hhxPGgNooofZxZQcuwfiS5j8glRZw7C9nU2Rhf0_LFlk1xl_Aj8QjSnDuY-WNRZMj3m1PxRvYlyA3UfOJnVNC5eh8l7LxpAXPKpoXYdGMT4w-vDeim_0npXGlWAj6KpFWD-sI2d9dp10wvMRI1wSfOFgHVFGIa55xcg-U0aiagcp-Z0G80WCSjY6pNvhJdk_BG5H-yKgt7qP2OCXlF-R6gZbowaMJcvS_5J7Kpq-4IaS5ibgkxvlDaBQvpP6D3pHaM_fcX2tKc10EHl3AaBCDnJ5RgSrChnqGQraN6WUDx1T9bT67DvFhno9NOkHh72KRLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bH1lioBfVw3p_PBo5FcuMsmhMrljdL0Cnel0HSntq00Gh_5z4ofkV8flNIvSYw2K4WTWEL2yXKMWgLH5Jg8V_8_FOS0yAH5eyv3i57E7A1Evcsd23HdbbJ_nUYgmWvqc4cP5qV_1PN7U2YwDD34UMROCC00UTs1RKX6qQER_JNZtZ449DcbC-lC4HrqCagZCSlHk2Pjl9dG9dZkqOxUJVw8qERWx1bq5dLD3Js4HMDThNbgBp4ATf_Fu8Mju_Jm87qVhlL9zvQrhYo0e9In-859HXJ3zaRWwqc2Z1Ax-NhOcGJ_mwsNFRNgsHVfrmmD5ScOEbcQcy2Zl38xqc_4lMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PW9aajazuZVa0_yze6rMxUpRGMqU3vhNyrzpI5_84msYYe9gP1y3KzLEM4iYNxGDKUVv0VX9BBLa-6KemaUyTNu6zd39v3r9jA9nfekUEuqdXF11rPb06Fe43yoafWOj0xYr1K1ilIHbxGkWuN4JqO2hSxzszBbXFPwoYr_gNrXsslRCRF3_0QKlbMTFVjyfP1_m-R6R5mXHOhrON3ujv_TWqTwHY9sBMuP-P4llQl_X1_zAshVZvE-QiXK0muxuxe_CuN2qyNWyAmOUCxkskzr04Tb2ysEh1XFRWdRRTxQ7elmDQNbzs9X73WSR49-alRg2FkCWjSFIxl6MV9YODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilfTiB-pOg66LfLYHhnvOfREqK3A-_0NWlpb6P7d_wq5lIvpt3baA58dC73phX7Jlx_JLW-cifEhKuGqpB5VfoLFVoSHQzv2k2y6m6ktOlTei6PHhq2hRHByUIduZ4i49tMavEKqlyIAZGl0s2_Pfws9x-nVtcbIt7LHHeij1z4A8guiZnash-CMS_YpVskM5xIvlmjLKX5nyu9KDVLGFKiSxgasCNeALie4GE_aZGAcZis7qVx9greNjbrMf4ds_H77_FeV8Qps7soE8swoUGVlwKONJNzk54G-8CsD2lQyB-4RLMzIVzQQIaa3-tVSvNgxFOfDEWnoXsQVS2x1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHg-zvkK5Icvw53fJf0AHEnAaIv7ZqEvEJGExHL4Ej4Xh4lrCsWP_vO7mZBeLEsfhuBIvmb16Sfwflp84vqQ9tW8bGORl9a-GMlCfC7JIvs2j14NFI0C5xvm0A3chrSGM1iZ_VMw0-d0T7iPhD2JmA6JTA95lsOm_nEmEJxtEDqciOYUxa3oiBAT6K3xm-NuC4lGQhnhC3-G32tYBG0okN93nLSGHGHtKTw5cLgNp_ecxrc8enpx534I0j2GXS960OIEK3leHZHv8NsS5g2fUxw2cqkJtZEBRvAuvrKI6o58QSJX5SbFaSi-HJvOyFsXs94plTarV6TMeI1P6osnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gbt1NzjRR7a1_ATFlPpLVpqX0huWSaZAzGkxNwVJUJPOR_AX_4P55Rc3zHFF4FeqoEq0OiaRqeOkAeOO5pYYng3DaHAF8ZUxsreXKMHJiUlcFrp6W8rFVAu7mz34PQO9kExoh_p-YjothxyteyBMiJMUj6Tb5zXQ-_aoFBso1NwPjX0dm1pLdqFXRUbomTaqUZyLXxfLEQ-KjjVh0396paOtOvDpMlu558-SWphjHuI9Nnnz3HZ2_gy3jULMQScjMNJs99sqA5q-yHlNC91MXqlb-aKnrRzgDQPDyBuk2RngLvfPC5biFpFF3ARV3v1KmkHD0QhCcAz3mBIaKb6GVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJh0A4eEuXId13jWEbokkuqwagSYS5PwRHQlA1g-zCYSOzaODhL5MBLbduEN2TwS_lTX0xhi13bQrOmveSisOqDSBKOZKybALpxxiZG8kej2rXPLbrDzGulMviEe8e88-Y-u6nY8zfhvxggO7G10NXkJ10URbKNW0CHv1FthrBdTXGqtwilU5stV068Fkhpif9vvf_btOn027dOTrMpYkLDUFIoLxaw7D7pcPe3R78hEdmp5-DsCQbWhIfv__82BUfycYiFQvP1ycVz47rl6EhcioGW-_MioTnFBouDZLCVLWi-uhZVpysSqXcOsZUDhTeXfoxsfrpqFtwVGoO29dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=EeGxZvFfmxdu2yGxbL5zBs-nEvWScwjIcIJ5JEwJL07-v0hLxojL4pMgfJ6AticoY-UTG9j_owsrf1EKlkCYmID5F1OVq8bAhDY34-PfNRsuKN7yWzbgHlOjlaSOp3hjFt9LszZzCLFvWMy5kpb8hwlSANKKoAAKM7dd7Tzn11F1LikpiWtjyHSM5ITSBmDW1QMoReOrc5LTca_QkJ9NSM0A6VQ2TJqb2CqyIZbBTOYq_EgoyMcf8MnGZAGnkYz9vq3El6neq7Kx2At-swns0VnUGdy0sLgMmEw0z-Y7a0rH1N4-6DhyzCbph3fwbDYE9r-XAci3kwstRJn4KRgfcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=EeGxZvFfmxdu2yGxbL5zBs-nEvWScwjIcIJ5JEwJL07-v0hLxojL4pMgfJ6AticoY-UTG9j_owsrf1EKlkCYmID5F1OVq8bAhDY34-PfNRsuKN7yWzbgHlOjlaSOp3hjFt9LszZzCLFvWMy5kpb8hwlSANKKoAAKM7dd7Tzn11F1LikpiWtjyHSM5ITSBmDW1QMoReOrc5LTca_QkJ9NSM0A6VQ2TJqb2CqyIZbBTOYq_EgoyMcf8MnGZAGnkYz9vq3El6neq7Kx2At-swns0VnUGdy0sLgMmEw0z-Y7a0rH1N4-6DhyzCbph3fwbDYE9r-XAci3kwstRJn4KRgfcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfksILGmgWpMc5okJJmzz6AtaGmwjkWslMV6eYvikzAlU83IBmKw5UL9OgCGRExTEV5OWuv-qx7uH3XEKCmkFaVG0BJhipxo_Jd5WJzViWl2RCOIXav308WZEw-mP8ZZ9I4L6mi3yNdh2KS1rUVkjHKrYLUhGEHtTlLRnqUSBhsQh_m0CV2Hr_X8AqiuKquHgQ6YoPQ8Hq2mEjZKGwTW5YSxAFdCEo6b3NOCUGoJca0fY8r2njUMoKExpa1qp8dVj2DQFnkjCU1uGRmYSbilRfk0UT2REr-tnr2JvFEnztpSc0TLkU6Ta4fTKiyhHCSpX8xAgHpGpav9S1pG7QdDAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c57jOEzhBXhzJ5geuEk5gUTHcBqEBud_MBtx9toBY4SLomiR2DqLrS82DNXRhq2isqvX7zU4Ip4fsdGH3Uf5oBytlqq2x8PzjQWOJQElysRllUUxbVkGQjSbML4h8PnUVuDeJTsHcienN6TBzSR7hcd8k4G9-iGiL-EpseqSgRTzE48iSRA1m9H2sgiakcduJKlhLu-NiajKy-ATDL9IXG1nWjyvo_E-Kcvfxm5KKVy3Ypt0QcUkjvfGnhzmM_tW9wun2J7PBgOQjDaAf89mz12M_7ysPnTUStulq6qkPc5r-MaWlwsJ0LRo8pb1iufx4rAMIy53rOs6oreycCDPiQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=dMgpKXJjtS73pvTyHMiAu4fGc3_rU8j2jT0KszB-uO_-15XlU25BAnhz6iuaN083M7f79yqJKztjujB1xfjZM_TSQBxelkXNvjF8simSJQUjugPq1muAnMRx3qEwu7wmQGHe91hWJcmyv_OArfp3tp-A3QSodJHgEx0twdjNoKD7eNWJY0H4btDcAx26K6Uu2ISTfbgZ69clROwz5e4gZV7SN-Lzz-3jczw5Ebeezvdcg3fsvoadFSj4Y1wGfAbJF4PZZuN5SzjxvbUzg-Ur-VnwsHNaxVUfEk7gcxAB2IpZTVGCMHV4DYWsZajjppir5PFUw4v4D4QZToXi1ez_Bj1yRBIKOvyUYaG5w6W5ux38AVbloVCD1ZMqfH1dXOL5LGt2qxLK-PcMSvd146Py0_sSeHrPqCeqq69T2_J0gPhiFOexrm0uhaG_XtclHC9m-0mbQXddXajEt9eZtiJZ3wViAU3Gg8ftef24Eu_h60G6outh1gzmRnRfHZiH9rFCmZ_Fw3fosG2y9L9kUu8Uh_Ril9b7Ey7E5WQQpBBz7JhhDKou1jvg_7XBsbQ4WYwPRB_sWn_GMJuCkTv1MJuWZWMXvrOoHX_1uKRvmc21DYFxxPCtluOaA0h7avqekqKrAQOIqVHE67HXV7LOInktCiSZwOykdV3rgZXhGrn_QQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=dMgpKXJjtS73pvTyHMiAu4fGc3_rU8j2jT0KszB-uO_-15XlU25BAnhz6iuaN083M7f79yqJKztjujB1xfjZM_TSQBxelkXNvjF8simSJQUjugPq1muAnMRx3qEwu7wmQGHe91hWJcmyv_OArfp3tp-A3QSodJHgEx0twdjNoKD7eNWJY0H4btDcAx26K6Uu2ISTfbgZ69clROwz5e4gZV7SN-Lzz-3jczw5Ebeezvdcg3fsvoadFSj4Y1wGfAbJF4PZZuN5SzjxvbUzg-Ur-VnwsHNaxVUfEk7gcxAB2IpZTVGCMHV4DYWsZajjppir5PFUw4v4D4QZToXi1ez_Bj1yRBIKOvyUYaG5w6W5ux38AVbloVCD1ZMqfH1dXOL5LGt2qxLK-PcMSvd146Py0_sSeHrPqCeqq69T2_J0gPhiFOexrm0uhaG_XtclHC9m-0mbQXddXajEt9eZtiJZ3wViAU3Gg8ftef24Eu_h60G6outh1gzmRnRfHZiH9rFCmZ_Fw3fosG2y9L9kUu8Uh_Ril9b7Ey7E5WQQpBBz7JhhDKou1jvg_7XBsbQ4WYwPRB_sWn_GMJuCkTv1MJuWZWMXvrOoHX_1uKRvmc21DYFxxPCtluOaA0h7avqekqKrAQOIqVHE67HXV7LOInktCiSZwOykdV3rgZXhGrn_QQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3Hde3LQg7pA2LVEc32tT8Lby7Ip-KI1TSWeNPCHz8hI_Z5hIvS7uXaRN_ttf4-IeleoW__dA3nCgQ3i6AjMK53G3TABaFt-OPhhrJmXVksyq8f8_TGNGIr69nIFGMJrsJpRqOAwyzRnsorJFr4TWUNhpq_bLCrpty3NMq0W0ITf8iYC2HPR_bCfvLP-fXRDbWoliJMH5pvmVmZmPkmhI-dwaFyhceg492sRTRpShcr5l1o2azaP-RuEaA-1HMjfdbg1SLtRhNRfRm2TAaT8JepoIqB1ejoIsKqm6yddHSylhW8vO45IMJzQN_vFqjtiICTI6Xq1YaDwvxnEf_kU_A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=ZVNXOLVCWy_gstMkfYBjaA534jrCzOVJWnniuZecFuKOYu-f6Dj6EpbSSAFtpfHQAGj4ebqWQSIznYouhCQO9kc-e-6OIpBjnf2WTOFL_23GwBTQU_Vpv8dfPHYQwjpM5epvkXTcjdRzboy7plxnHwHbmmrXvcKtDFRa6M7_vFjfPhGb3YpZYXAB2Bv3T53sY3HlMtKtSPlcfWk_nx_NM0LZBuSOFotfndI1L45wtzV3j23OaeB0H3IKhcj714c-MWh6tDXR_KpItwVnIUqPxYZ4xw-Dff4OtH1V4o0ErQ1kQrYBh99xmDcSCVRtfYCga-DOwZSAFDrgumLfgqOTRxZMCaPY6mjLGAzXLTKrkmxPn_Rb56cTun3j93mMy10B_WrwmpJi7cCtljIxpNBf9AEzWfMzr6PUtyOtFmtsVZvcQyvdksaH-eHse5RYhQhACPskdoLPFwIFh07MX6jfJt9kD337o9bo9VxZkRnpbJEcxvV59iwQ67jSJ5TJ7__gvgOfKDcxowpxlvEwMyfd_9wHSo319h0XU-TYnkGko4rb0X_GP-gzuLuA6BaZIpLJ4U6QepuNiQju0nfbTg1QzgxgJNa-qG-vY9qOEQSDf6mHrBOyvIvJfuFA224ZMgqGbcWrvk8STkTfjZdM7FxV6NQ6UwRrm4I9FLXs17xhy_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=ZVNXOLVCWy_gstMkfYBjaA534jrCzOVJWnniuZecFuKOYu-f6Dj6EpbSSAFtpfHQAGj4ebqWQSIznYouhCQO9kc-e-6OIpBjnf2WTOFL_23GwBTQU_Vpv8dfPHYQwjpM5epvkXTcjdRzboy7plxnHwHbmmrXvcKtDFRa6M7_vFjfPhGb3YpZYXAB2Bv3T53sY3HlMtKtSPlcfWk_nx_NM0LZBuSOFotfndI1L45wtzV3j23OaeB0H3IKhcj714c-MWh6tDXR_KpItwVnIUqPxYZ4xw-Dff4OtH1V4o0ErQ1kQrYBh99xmDcSCVRtfYCga-DOwZSAFDrgumLfgqOTRxZMCaPY6mjLGAzXLTKrkmxPn_Rb56cTun3j93mMy10B_WrwmpJi7cCtljIxpNBf9AEzWfMzr6PUtyOtFmtsVZvcQyvdksaH-eHse5RYhQhACPskdoLPFwIFh07MX6jfJt9kD337o9bo9VxZkRnpbJEcxvV59iwQ67jSJ5TJ7__gvgOfKDcxowpxlvEwMyfd_9wHSo319h0XU-TYnkGko4rb0X_GP-gzuLuA6BaZIpLJ4U6QepuNiQju0nfbTg1QzgxgJNa-qG-vY9qOEQSDf6mHrBOyvIvJfuFA224ZMgqGbcWrvk8STkTfjZdM7FxV6NQ6UwRrm4I9FLXs17xhy_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoS0fNwpmQ3hqnFVniGDvgEAwznt3VAKWwZGEPBi58ijMK2e0kFhkIMbdzoANkV5vLbkBA3uNF2-foHzU4HgmxKqTKl7y55OeaMkAT8P23zTk8zobJ_GDL3Ja6MIICJfcSspkTWn9f1jLxidvGUGkAnvxSzdZ96TrytrF00Jzht21OU-9vs9ighN0Z06w1egOQuSVFV1IMoAB8vXzbA-vlPkPCopy1EqtAyWHY7Iij6p5GltzpkFn6yeCFSXV9Iqj7C__5-qXhNL64Rxy29UyxE2Spqyc_xyGYkrzUA2HuhsUPshNE6UuKmTI7e8_arhWf_8ZdHN0qXl738AGYwx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UumuRflqU_v_cXjCLOrXMipTSPZ0yh1uOpBdDTOwFKWJUYU6eAQ8BCsaZnwYzDwgL-Qlji4VWjlT2wgl8BDzR15En-HqcXfKz_InFCUVw_w1vGaurpHQVSKOUA5BH2-EscOjL1NM2HEshFe33P61XwUHTMuqJEaNGSHHCWsXQPUheM9a0CSUKZnpeE7wCZqdo6AeX29sFx4f0O4O9M7faRmi-pW8sytduPiMwIcbOdjByukEkBRPxKcyC_WxUhmVnGTqXIqlvlJuQv3aQEoFRkr0tKCThDtHA8fuYvluWgLPOspTDTpx2u1T-MOnzPG6Ztcsxguoz7cnMlL-9NJwrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol2_2IVVLWIpDeoghKz652WlXrHC3J-xPBbmN7IaRd5oe65XmJW2h9kKRM88zhzusH2GjIaM5J0b3OrAEi8v6BoMOcXzBsoR9EbQ0s0v5lW_zrGLw_Jrf_uklbboJgTF4b3jLv6vpugBmHRXugKW-y7m8xPEOaFGJzxXTqmeERSDWZeEV_aZqshF5ZmRMqbZtTESvYk8pIMDS_AJzFnYtjcoALYScBU6oCPwrKlIKtvTwWBiSa43p4W-x-jzVdYTfGw0lDUkLoXsxLk6Sv8XoMJeXi3sPTAgUsMuaFQCISqbPiMxh-IUhLZjp0CCFTFTFBoemyKUN2wcKsxMcgvfjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQd6C9s_LTj2Sxk8Zx5yDOdV6IvGvx_pIdtXzQlzpSUPz9cxoWghm0lEBX-vWiqwj91C-wXxlewqIDOS7tMyXvV79OWOtdGCgQtzP3HRbm9CsPYnJWDu0lqHvYjMj4tr3XdsdS8torVRF5HQFZqdl8OgaUDRcr7FxmfawQu9VIq8ksqGD28-4iQCLxyKyjXI3RU-J5itIwEGMPLBMDacypVQWoL1wrVE1Nw1t14JtSiXTDapuus6PaKMMstZqRlsngnU-OGHc2FzWxGdkBpPXhuCZt--zhNNUNlbk7pg0J6FS6CtMMcxL4jWcvWl9zjIM4a6VLHdNuMD3lMu5Sa_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwxKhWnjiD3yewKCB4hzzt6FyxwSpYh3wPbEFtfsW1xryOyAoYUd7E1BIbpjlx2N5Eb6A0zJdziHLkhuer-7oPy9RhV4XRGWSKR_pXLWA-ULAu_djmD8-DkyqQPffjlwjAuUtPgIOmjUyknG6lbhyE3_Y1O90inbZR3SGHmZmdgtNRGxYucz7Wz-55pzVK3eJe8HBXDF68rn6kaB8IVQAHg2cGWfGk5rZ8XDhIJ9_tjlGCj8wEZBNYJIDWx_6EhHsC_31Ub_sWsSGXl4rC9WGyP6Hv8GhpxFsaWssqOH9O8SlSwHvTX2T77KqdCJM73sgjv0Ns-aONZ4l-hMvRrLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SioDM1fDzpd2-Q2MI2U6NeJ5fPJpBlQYqynD1zbHjiiaVgOPrmTBLBcC4LidgiyxHAH6qLwpRMGsx8bVMnfEjT4S-rhp5j-iYroKXfU-IprK2qrY8roZxSMGddv-ZN-HStqjvFSfO0JSXKaLSqq3QDh7tW8_vODEmNKD737URvL-_U1NlQ95uYWaW-D-hin3BvAXVKTQnQaoLZRbjnxQqtUvGNhf5fQecVmHn0-60TL6j-77kMAqhuZLXvMlEGvZw8y_KpaHsO_hO8bCiXDOyyRNGKTz39KnApUVq7DbN-tvqBpDzr9AxwxoH9EI03FdEwl6qlHEPDgCMXut07O2Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_ibCnLBHM81qcG7xWojpwWjii7E34rXOUG2sdA8Mx23lvjW9bveEdZfsPArEZS22IiWuXIBM3s7B5TsDz70P1DUwUDz-eUv8HPGF3LF544CTKqzGX7SxUFMX0VZ04fiDfHQHxsoL35D-9Db_yFnzbqmjgrhus6St06532I_jrWtaXKed8o7cVgHXOmwOW68M3gP1FpHHrsPXqTG-Cp4K70QQMJNqcE9sSMZmgUPvITuoHnqWywdRGr7tG3w18-8WepVs0RsNlQvc5l0yCx7OrBGuq81K35WYtF4kk7L8g7mm4IkoHAWG5d0vyOllLlhneLmi0mEq5nEAUtmIC8z1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlD85v3M_JhjEgWBXteeDrym7pmKo8nXU-yVsJsIrTzOq3_RCbtDAADi1B02U5hnA0fuMhepY2GbjxYrffWsKV4HEMtRzIRXBv43frro_hkpulcgHS8-VbbU-UrP454v4PLS43dVbE70k9BZvonyyK2zg3PeJ-qh48Pv1JOkGXXXp9iADYMOITRYfYXsyglJOZZasym5y3weyQQ0kyyGDADQXk7r1Rvg43ecdNwwh-ZPuz1NYViyIjpCQAinDR7ISi21VpfbsZI1p54Hh31Ab3Kj4Mu9BETp8S0-dC7IeaBDorXVmpg3tYRxo8mBeWpVxSB4orqBwPWM63y9YcSuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeuYdsuhH6BunYT-QxrX1bvezq8klNv3-hJtaweExfrcUoSMexCAiKpSa0oV6oWyhUJi6iK9-Uf4dQeUiCiP3IUxEsdkD5lgyAhhLehp1s7W1Zx3niq1Slp7X362ICPnBJHawkbCzKiNX3wLlYQS_HLEaeF_iYnyqJbTkoU0_9G8nIHwwuPbb9Sjsv6HyH3vkd8jhHNwxC5BDk5VUOPt0K1CSAqt0WX4xYWd4WFz7MKNJ9vPKTIxK_TUZXPQ8q7cfeCo_aNp0_7y-Y8HOUCUm-aIR1HkIFXduww81v7vf1CV85RyZVC1XV1fr4h3nKfOTaWUD1stYehWyc7omwlCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF1XSe_ORbS4ODhyTDDu9RQNVEKlW5Dy-RRLOFVzmu1CemyJiiRUm420F_g-92OX1Jtey8pVPUmQtO-LqFwS4oUHgdD15oJbRI-zagpxFwbHN2FkGNCcRoSfor3PynQfJDfC-2X4imo1c9FMMAGnGP9TLMBohvrnKsRG3p1aefcfShvnCTtmGVFoQHu_LoqNRNLTbBpmzo-kkOtD3S8rtT_xHojSf2zoJuCuyc4SB9HhnAf8CdMHeN55xVq-QyEs2zTGQcYgPXTRzmpulgkaQWCfInFl-h2kO1D57wJlDTZHlXbqZE7Dyh6iOODhiNutDZQ4KeKHqW0-GCdtEKLl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXuuju1cxcKMZ5WrwCvOMvJuWU0u2XyGoSG5wTZABhOydEGyCzxfzTscwU0jXdYKRZcLFl5r4GiPXHN4-mjuzmL9IaV57n_uez72jm0zKwdXHdNjGID5D5NRmaiPe0F4sUmFjNuwgy21lLUZ0s6hoiX7_rG5Em4ZstO0tilxZNzbl7F0-N1Qq3-F_XS6_JdrfoQkhdfzYFdXPXXPJ6316O7ykLJLsQJPOPLabhGBhAWKaViA_vaRJEh2JuNbhoPxlI3THpROg51PQJf_Q27k2xxjC7KVs4RrieC_ud2ovs9BygLAF2_Y__r9uiXG_nVrWzDAWj2vatfBZA0ptz-B2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu68yM9z42x8_zk6gLQ7Hs_U9l73pI7h9SJ1u93osMXEa6DfxWax1Cn8oNW7MrC8rkKLyuGST6fzgVF2fq7J_Bpdu1CyGSx9F5SMci0BurADk8Fxabuo-g7CeIyQqWWzSjZP6iDKGQ55RIJ3oFXHAuiHd_itqxFfZT5oGJt3Zmd3rxLKFZAWW7aSOV2jnWEXHusUbSUfuhqyIEndV4kQcSovuZO3EkLl3VV90eQzFQ5_E05lCCQMQdtZZWATLRjWkP4e3ZZshtP8A7yvXNfj1rMYqIs6eLPVPdIyIzd85tj28twOfyPnNMY_bqgiTt9JgqWDjC1JV32GOxX347UHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYGc7JeYE2YtQxVclw6ofbebZWkEnDUAQFpJiMgbyomRVOMdtjaqgZmUtWmNngCj_t_kLsARrAAAfNEs4RIc5H1a8Ug1B7BHwntMt6l_ouljrs2GfSgHJRl9Pr3bvPzCPyJ4gswtNeyZUYOsm9om8Xr1gKzRPF_R5IyjyBWlCf8CkXss1VYvKldiY79WU_B7lOMGEjeFY3uXPzN6nbskl16EzvRrKuYkYDGqwIEVZsqsY65n1J_zlXfwzM1frGoZGtFDAIk_OTeLjWE_HwZqb7B0LdLucRbsLKux7VOoGe01sHKV1iNV5WvyHGbEW17ujiTJtpf3VKpCGtU6DppNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyuH-4k_p__CBe6DXyQVPOEO_X6VOw7zlvoaOXDtmi8f5Lnias9D1bD-6obGscRhxac9zdMketTaA0UE9j-g2RUTzMKrCTbps0Yfa6OJBwiRd52ZmwIFDpE2IvolOhvNswCE5es_YL136hvIlRmPJGxwcosle2UihXK7fXcOQhEM3rYy0pRVokHIrWUSnbUGR6sYKWnn-GJ_iIdF0eBEg5AxvHWedmlOKf5NHCS9HH9xrOPlUVmo0F7McAJ4kmUr-VWJPEAsPVN2RB_49nBr3G9yF-lHT_clvxedvmvCggZ1Rqz5ECAebtcTuwLOp77kRGp1oIKVlikKHzhdCmyKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvH-X1GiSTPqcWohmMQjTjpeYVDNCLePDKKdmLjOm0lhtJ-p4yczylEIuLuDco02wRO3gVR1E92eXCErEMTG-kV8OlEemPHiBEXWWrzzQFxj0pl8JuCV8hYIsf-XM2WnFMGYI03OHgIxNrSh85563YNdIi-GRQ6ob88mqOrM893trfs4pgRNudc1aqVideo5eLt2qLR-u6tVPX83_jvpb5eIwq36wzhRpLQp_MsDTPjn5YEJuE2QJrd_BuW35-5PTDQY4Tb5OANSTirxkPTIf3E71ajIqb8qtB8l6d880ri1clyUAfGWoHxz4qbmQQ78mPgyCJWHO6U9ildT1QKD8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyPbHYcY6Q14U7rkOwXsdHqKIt9tmQIDjYAvnIvmQCGkcShGPzisyEHdD_nNDorx9geicFoWTIsnF1G3SEJwO82dlW8CYGUfTrR_ttB5ddyOWOv9xhwNWw4WuGAzCMpNpivqHN0E4rdbLxYg4fcWoJx5_5pP5ht2bB3glWuBGhiG7_vKMiq4-jDKX9pX1tteciA-vpvJl0lSI0YaWuKtKnLZgGl19SnWaiqac1ApZchtovmspISSVJsLd9dYSzpKcJ4V4OCDxwsBIzdR5hujXnhptrzBGS_lI9ds5rWCOrrLQ1VzfMWwVe3LkrIUroC33ZJcYtWkMbWekAGp5V_Akw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag2_O5XoOKpPqY4lvAvz7HP53UE2sOiM0fPCANS5EIxhxWm1_8mEzA4d9dQWSUMS7ZGMrcLGUzGjyCdNXoHg4S2dunlgsFAwJGBT8xMEmW427P5o26vk0eMtTW9Rm1mUlb0HlBFoyGkzoS1QL_9dVkvPLPB-9q8xQLWK6PyJnSiGiIjh1jKlVU2odSkEhr5tCYsWWhdLnMU0zzRNE0GsgtHeTV8nIFQgrRZog6t84D_scXQbRLLeF8Spr5Ud-dPSdPQe4KxyE70x3tSG206s8sBe8xPbrSZQ9Q3W6749-g2QC6fbhDUx-wn48v_et90X5xxYK5kRo8RyueQ8qsM9rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hcg-HI1RndcpTfnjq-Zhj0nh_yjD9XMbvNbtUgUR-dNc2e50I5-uwgrGqhVNl0Czlrgne2PCCIBIv_DuxmuIJUd5Gc2x-GkwT-notlS7LDk0BQZ0LHbZ6UxhxwWtWcjq62DQcpdhBUYhX5LhiHYQoRKEj3jAlhoXgcoP9wkG28MQ6qzW746679kWsms98jTS6xwD-HVW0YJZqEJcnKGuIzT9fj75cU4I6K6T0FxdzgyD8JihUHOvLYoz-4m9zkjDmFY_ryLhmFipwvDn9pl61F8zplYehSKo90ywDn-qkhsqopReifOiD_vLXOXl0l6gPicNIEldijYWRJz6QEmlmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a75DjT79_0lrny4XtjamUhwoxwmRJwgvz-M5HR92280JuYeWbzzik1TGlUGJdS15V4HGv2GWB_yZ3FFXet6T4wXnKgBiNs-NUDCBM2LbzOKWDVVfUiU21m78VLwKz8zxRhCbTeWGQicGx6lFBKNMMLEaid757blbuXSiNKeeR2AMcIfGpJYmjJiy7y5F2L1u76rsTAT403FXU-ub2QyRcNtb3pBF_xQbNLis9s0kyTu2RKMIlHqbyb7D4iZHrwos_HT-JVjHg5MNM3Dw0y0rT41sBl7NaonL43taPatAkJ9um7FtPfblUestFxelyoAVSQYU2SFWjbHMAV02kXCm9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ES1kco30IRiPgisg9w8W_hTyciP0IgiFTGUdBqr1ARBumAWxCnIMdYN7DHGm2Gg7160xfbF9KN0lMe9QEh-J5T-KIHI6968KBaB9zKlBRVBLn9RguzMbzP2KcUsVHHj7_ACzBgJwJHnvxpKsYMrv0tunhLBJ5qDW8IU9RUHU5VYpOc8d5llsjDS9RX4x_00hwET7TeyLBI7UPPHsdWJD1uPuVhQXCsSuZSmhIqSw5A6WHQBjOTbTTKO_FXWPxeQ_vufXH5pyA-ilivBJZncSsBZTVCTC9xwEMIUMCYUjjiqUIhYyVK4AxCDJ6nvJ8QpcreuB2QJd_N_0S846piNFAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQtyZ0pc-cZRFCUS5S_oIhtVZbpU20_WFmHafM2gNckAeeHuJD_YGHXbPWIT2_qgFPuWiaJaX3hB5s7vCYBSl0MjRa7mWgNGnV5CNrVSLoaGaXY-vmhSc5mhcMKDbxd8pHU1woeX2wcJzr844k3K_zWuY8bngk1lHUCaQVvqfyACCieNgmp-lOJTJ5lwFitUxfEngKvkyMI7bSraJfse3igIH8SzPt7ZgyMhjSMFR2WvRv1Mi5xBiGMTh4VQpzUWhKB41BbsY0X_nwCUdt80zlYWwUaxqQmDIB9GQSVTSDCK_74s9Vgv3hYbrPgYfqnO7WaBZIjSJuGr48a8vzhxsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqAWCBMF2sAtZDgdncFfmbofyuQCWs9w-11LrBMcNvhsGD3CtTyK1yNHIzqOrgmO6wkvJvhDwGH6Lv7t1lAQ_fdDRNNMEYP-H1zLoNfCjmJoQ2MmtjHbHMi_qdhlxN1Bxd-M9Xu-T1ydSgOl-tTfXOdKXS09Bdeu8lj5pqdFkVvht8I3dvP5APiCEmo6BW6-bbqbs6SwKBigkLJJ-Jm0nYcrCOqoAAV6pZw5cVBF6HRf3CMkoJm65EBCdOLqUKmDdJbSmO2OqHobC5EmgSREVRkjRBhTL8m8eeVJuZuMNzt4Ls3-SYKGaVdnHkdI5tV9uo9gFzTCz9Ojqia-MGSDmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiYXmbofqrYV76vskHQ7oiCZy6BAJMNw9-2AW2cr09VkuDl6po1uyaG_U7y1D3Jk1BSamEsz9_Kcai3gltsEEEwJmdcpovoSO1mwfHvrO_ixpCj-h3P5R69sZkO3c39Uzsg6iMg_xGTNKLzBJ8_hNeIdNvjITwMNquPWVE9pwImTMbDty-YHCmRObHuouDr34UZstkGxK-06GdzuAOOxCaPaC4eukGa5Fqy4drTIn9rR459HnAcMaPi7BYIPXI8gB3tAzy7VA7vC3Sw--STYia4GsJMuPJS6luJdOllNb_oOtZk5K6zPMxXeV3D634RtDq4W5z7Ox5mh_1A_xma_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
