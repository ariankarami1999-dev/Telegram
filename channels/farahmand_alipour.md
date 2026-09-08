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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=VvvUUHiEG6776jFjM_ItS2iBYfweLKLhGSesZyTAcKV3SGkZaqQIZVqjju7iSovccwgY0oTjKz7JL493OnH63fixx7XD7pm9DI489-nLMm5EK5ajyLFl00Nz5h5DK7YpqATjGaUvtgh9-U0pU9ATyCDX5mNTEXleQzlYv74Y10BPBqh4_TSkUp9x0WQPysERJaCZDFmFzrp1Q0Em-hsyNJr3HGs2xDFvj8UXDPxaiMHnXpNWbDfwK3UPVuO7g3ajJ2qxyzv4BndqlHAKUsI1KZc549HGZLx8WxcY9Azn-zuhY_cqEAze4eR6uF86n17eeb_SOkNvagGdAmc53syvVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=VvvUUHiEG6776jFjM_ItS2iBYfweLKLhGSesZyTAcKV3SGkZaqQIZVqjju7iSovccwgY0oTjKz7JL493OnH63fixx7XD7pm9DI489-nLMm5EK5ajyLFl00Nz5h5DK7YpqATjGaUvtgh9-U0pU9ATyCDX5mNTEXleQzlYv74Y10BPBqh4_TSkUp9x0WQPysERJaCZDFmFzrp1Q0Em-hsyNJr3HGs2xDFvj8UXDPxaiMHnXpNWbDfwK3UPVuO7g3ajJ2qxyzv4BndqlHAKUsI1KZc549HGZLx8WxcY9Azn-zuhY_cqEAze4eR6uF86n17eeb_SOkNvagGdAmc53syvVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq-qDV0w8shy1jeStwRMjipA5gfNDIRI8XMxAOz-q_idAjTng132C-4UArq6B7zAQMLHXGTgBenZF1QKIOy00Em9qsZWRF-kJl94uzcgTKBNSEbPpICnVquRW6Kx8eUc7l7NLMm28gyRakV0mNtsicbYFWl8Gj_OmObqtpEQk5K3_c3scZAvagPdmMIOeKNwkywVNGeiDA42SLRODO9VwOBxJ6rIJXcQtYhFO0JLrXKaEAJWXI5b-9E5I0-VjLFLdN7_HlZCd4ykb7HjudtQ5sl88ltn5ICBQavnQSQntCohyaQVP35vRsxFwfO5Hln5dzgS1juagzV11fzNJYkwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miiLO1r7IhZXHOHScX02__s1QXOxCCQA7vQCZEBq8liAVW3NwWAO95z9W1K3CY11fBmj9dc5obYwTvp7bM_7WD-Ql0UVDYhDBVrmgd5ZrbcjpM88abjamkyD1VyfxX1hBm7UUfLVbwys8vlVuxclRd9EzgB8PJSf_NsBRqurv6UbY4pn8zahbqlEzHCYuk_5At-zNBKOMB9b1YuRGDIcJrMzBlM1yvJYuUu2WMJr169T17ycDEd0pzlg1_uHQb6y7AHv5Km771YFioXRWiu_4PqZy2Aj7lqqGK93CnCDA2t6mMx52DsDMB8qR-ZZctgeGSYE2530eMQSvQImeLhVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4xkZvDe_TRochKG9OElTNQ5FAOZmPVCju0xMPY-N94c-UFq4HoE8LgngXeU_YDXVu01NzSHQEwHHaU-AoLT74htlRTVs2SHjeMHcBdS9DePygfhIAvKB0CBuZm5JJbqhxNd5ras9zBrC96cKDy5Aqs5wrXV2x0n9MEgY2vjcbQibhAoyxDJp0xkR_4JV4GRcw6suy1uCwS3ASKZLNrPNHAy-Vb5WbaBCml85UQbxY2e5tABQbEKg_nMSqPiBRFFss4YAZ56EK4CXp3Rx4EoPg137Cg9VNndQh-K_yWdBIclcfKZuUFmZHL_dLj3m3zuRumHI5lbjeZGBCpEfPaBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isIGJ5D_tk1ZcSbWxM6aQrpEHu_gWrTruUYjfCeRwzykKI9pp4evymR5ujZE7kAvrR1_4jFVDl5B7WACGbtcVGulhFSRLwSAjTEKpwaHp3r1_O-9csNYLcsGcYq3rxQbawho_8okLr3E0kY6vLARhqng_3gwa1SrHGp5FDpI8wyS4_1KizDBEFEKc3ZnAbLf2a7p2v5WyqU7E_YzK4AT5hz9OReneEwWVqR-tpYePzR0O-fSx4LMZlN5-BCGC7ZzOanALPxwnVdLqTaZVc1aiOzcEUnAqDiYLgz64e9N6emTwRVKr9nDUM2pBuHUKJiMO48UY2io1VCKhGtwBztx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ibGdmBi6PLoPZu3DCT5XJ_K6EHEx7b9K8THgdl3V-mMmgtiBGo9BGGyiCHmLeDtxzgtWjpkPiZLsPm5rE00KvGsr1n3-BPldjK0KeO9SQPCEXS_3DivZNZhjIgWh6rXZfEEMWxJlqKx36aMiTEhEGVeE_IUhtlmoiRlTKrR3C3Su3uYysqBe1chUUpc1HnWoDp7aq9LifwZmkE-pSd9sSL6eBBiftJiaaGqWm8Uw1eaKzTeSPj3M_Cb3ehU6Xpt56wbtn0lONuna0rKiPcvxseLzF9hAS6I95dZhJwChPphOrYeDgUoVAWKo5a2Y2upAlMtAgf12pAGxRv8Rti1LNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ibGdmBi6PLoPZu3DCT5XJ_K6EHEx7b9K8THgdl3V-mMmgtiBGo9BGGyiCHmLeDtxzgtWjpkPiZLsPm5rE00KvGsr1n3-BPldjK0KeO9SQPCEXS_3DivZNZhjIgWh6rXZfEEMWxJlqKx36aMiTEhEGVeE_IUhtlmoiRlTKrR3C3Su3uYysqBe1chUUpc1HnWoDp7aq9LifwZmkE-pSd9sSL6eBBiftJiaaGqWm8Uw1eaKzTeSPj3M_Cb3ehU6Xpt56wbtn0lONuna0rKiPcvxseLzF9hAS6I95dZhJwChPphOrYeDgUoVAWKo5a2Y2upAlMtAgf12pAGxRv8Rti1LNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjH0OUoXFvM4O0N1SO5pyFsUkrVH1OwySGlhC-QyOHLEdQmjBfRdBBj82TN6JoX6Ox5whZrVQENB-zUK-b3lOyt-uyYYyf3t6m3VGQ_j9azTCHpsA4CJAZvDuC4QjcD-UFV5y5p0GhcqzRTmiJ_yhXjcy_hUT09n5xiJNxIslnKsLhEf4yXguev30cx662TagjbdP2rXfTJhucmYB2hVQ-3wr_RRlzVVKgX1FA-ysuEWA6EtLVOIPYNSRjI0LMi760FvRpD5qp6ELkuZAlBdOmfprRqbM03pLBN1XEcCve7kNAYvdUTcySapM4r816SjqUXXcj0BxsYcMALCDQQUyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpUlTpZqEkqcMsU30d80GJEaHk47fhWAvZrGgbRGpWwMcgOVgDYQHlkl2LIRPzdSfpvS1iVylRpUcC2SkElZvJeQDz-LiW1fyte6V8ee3QX9pIjYRoB1MHIW739eiUaO4Zoq5c0U5bruthJD4d6D4W9njP-TWJeovX4Pj67rAJB8nqBbcE8MUu8gyHHZxdNrEFV9y60zms1_wLwKVvPZGiXJrQTe_TXzTVyxROc9WpuKxaDxZWNttGWR-4ArKaBJStSRMyBPMBWQWA01MhspZ9lV_iKo3eO_oxheECorXDKf6yHdeLm0-VNG9cG15Qg25o1tffbZi_v-J99ZrsxV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIc38ladL_ci2ELoAcaihO4pUGnWeTEaQFFzLwrQ2W5zS-2BOMb6E6hqggTqAXrbHKSRt1QGiJSnCjWELvggsIHzTuUrXDMchVXsj0itri37n9TPcl_6L01caz0OAoBPo2sz-JnKFAd8sp9fZy6WIQxggt05X9wqOpYAsYMEmrTyN7JRqYOLEfJ1pew9dJQLXYvrMrHhTfbprume2YFZzNgAN8oCLCdJ7HjneFFdlauhwucl8hYpigj6Is1YeplZPYuC4MkmCD5_iaY9dqTO3IAxqRIWsV91Jmk7M2TjBCp8qouLwiYZKJz326jLtXiguoCfK1xenGQk3BHgoVgR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS7YkWYyXByLQc1uz4pSunxLock_Y1SMZCgrfiCbSBe-IymW7rdygEhTx2_4uLDuZsg1u5i6NwBy8xPVTWPxjzEKqcGBa0OzG6lIDMyhKpTpMgIOqkBd1B08awh5dOwqc7pktxLH1u2UVu2kvuLBAZTaCD1QkEtRLRmNd458rQWjt06h6nKBZks1Kz_fXc6HjGO4gpW2VY9vXwih4losVUae0d5-gMSsrJgDHgNE3YEJTXQDZxgEIRQmwEo-1eJ2Fngda_rLcDlzFwE_AiTMHNRantTBaKhp1A5DOZ77g7GsBbd5eYBB_SCvHf1N5_YOjudJnBf6gqQa2Pe1GvNCQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFss4HVa_7xZWhNatoB8Vts-EEGtJReTrnrWbCbfQQIXX-6HP2ba2m4cv-1HIal83t84zPt1yquvf4H2l0L80gq_WvZjI8MkNWNP5oxOqPnVWAF2d95wBLe4Z-ugwO0LYwEv3wy96TpbItcxIcgkgc8KgDfzguYKr5riS9i_NoJfOj1bGcveGMgrnN34GZNh-szUrKn1g195HY56hxneMGcAjVmfOnsHO1ccIEIAX1C2bEK3bc-uBQ973QAqH6oPVXq8uojXYFyAHv7Np_7toB6WqdCExRcI_ux9XuC9YJFmEQr_RJlunXHOi5-Zk-PH0-c9NiZNZt9fd70rCnZcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpfTo6UK-gyyyyT34Lh1oGP21qaOn9-RJH0eeVsf_O013QnfZIu9n4r6i7vlCQBQgrxuf2ddDNZe__FK-vR0MHVH1zNdh4LTFP4w187qEr7ZrCBgvTkwflaB50peUlT3StNTND5AYAW1lOXhQ1dINhZ7Ok4tCQe29Sk82HHbdTWswZGs5qwU2fOQDyEBGSUmL4sLA1lmIUt5pfoBQArAoXtK0p8ZLSxCF0t0vclc6qOA_WCTYDNu2xwRt0IPiUQ-BriOi4RWuIe8Mut4eVo6XGZsrJvfhS7EGBqbGtJCPpLOvFFWu5xnoxI3PZRTQjBl_zHWZxf2zFyLnespnemjBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsS72MfNDa8EX-1TSPP5jtN66qWnbaMXnm-Ixy3nGmEgw9ai3uhQIuO1dH-CjLTA9O1PdlC4qw0y0OdnNpQgj6zUKI3X3QR2Z36uiK97f_FmgDABNFCtGxFfNAbNfjsKcSsJOzs74VSeewyMO1_Qvx9hKY672E3mdBGiv0lLqQJ1GT8fMVN2z80GKjFyJdgQOxWp7-84jtGtRzNaqcg4QwKfhFXVsrv04vFYhxuC1MmnHJpWmjVzke1083nlckZXho06ywxSYtT1-Ab9QXKsfPk2Xd3J5afPxNOO-Gh1xeSilpRlI3wZ8mx_m-h3s2sbxZtM3tHI8xXrJJqqOl8VeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IdNICZVdy9r5S1Pvv58Xr7pkZzElBqbukbtOMvdk6qRU7nRo2j_Ddj2eLodaUtl_b0iNGm6j7VRU-QJHJM5boXsGpMegt0F7Ggz8Uhr4KVwB-x3ZqAbq9m_goBZxXOcG1PRUXb6N0tvzG7OBeNsAntf1uPOHo9OiutxvODihFi46k-tx8GvM-YX9OM5GvYB_t8exlEFO9ANgJBlXrFdhf9xQVynzjvyeOcjpUgpdMRgh3gvMwX6vlNaZxwIMjEnMh1hPg1kGNLLZHf7Z2JJQ0k4dPi2pLb1OHDhDGvo6ilyUA7m4Nw4TDuA4V0hU-GaWRVwbSgNoiBwX-kgenIobsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbtSghYWKyZOM_tXd6Ih05KVXJkTKKDJspxqTCxn_PXJbHvd_JAF2JQJGlTH6acg3Rt23wDeqHaZ6tcUSh-JcRVubaNWEOOpKLY3rQ_wXwfGN5SaxocsSClphedW7XYiR1CC6bC1EajJQhdu-6rC29GYu6GsC3vIkBp1FjivoynB41A6WEgnhBHEDj2ITgksYRdJk2aB3opIiia1MZQWHOsnnz7ZyIYLUuQemcdUjR2-6xLvhFUP03_tb36k1DcWqJtWQIbdwuHs9MN1oep9uCodq2rlMFLV8gDyjCTTegE9Fjtb1b0TSBKnulSKHHeIl-GVOV2Zyt9nSqQoOKRJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OU-C_TPM8VI0VqqdUBU0dbbUSEDngtQ4SC6_6o_iHu6QMZOZLZAqN82hSsZ-bm1hCbd1tiEqbSGNoL30S9Vbt8z_8FqxGgCj6NaoYSOu3WfS8TZlKD4TNDyD3zUhJBXarZb9ITPqjMy9a8muzNlUi9iKvyPi7G_OomOWxt2GtOT6K_AG6hefKLz559UPzog0FwHk5TNiRNt_2TZENYUm6i-iAasR02bCoIMc5aHODg2K4b917dXCcqs9MkkBHPZ1ZfMYOLAfxF9jNvfuhLzXCMhGFK_7VB3xjvtYgq60CR3-1cR3lMmNTXof3AvaGL9Ae9pVKOJuUGdayGWmPe--NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=t8yOgpJaMyC6u4GEsk9AGhW6pQhwEz9NOpOMB7hc_OyI2wlvTVIFBCUwJ2EJS0kvVmoiUXfBgoArs6-BE7yrFHtw2k7nJwo0zb3qyrlNyzC8nNUIXnvUYTjtSnkiUCJzkWA6qzduLlDkJ5GTplyKH2BVIeWtX4jpKhvnFUn2egrLbEXnlf8-7hfy9VldaMuyUqxJ8aukYUw3GvZ0dqUYTfV9ngRfiICQJfw5MjPNoLG5CMNDn-HZ2xTdEhDH4az9DpZGxS92gxvIk4CgpGq8MPMWwpWBbazMNzzDRrlRwgQdZmd1hA57O-pnZH_lBUr4MhgqYBKrGbmzMRhdCX1M3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=t8yOgpJaMyC6u4GEsk9AGhW6pQhwEz9NOpOMB7hc_OyI2wlvTVIFBCUwJ2EJS0kvVmoiUXfBgoArs6-BE7yrFHtw2k7nJwo0zb3qyrlNyzC8nNUIXnvUYTjtSnkiUCJzkWA6qzduLlDkJ5GTplyKH2BVIeWtX4jpKhvnFUn2egrLbEXnlf8-7hfy9VldaMuyUqxJ8aukYUw3GvZ0dqUYTfV9ngRfiICQJfw5MjPNoLG5CMNDn-HZ2xTdEhDH4az9DpZGxS92gxvIk4CgpGq8MPMWwpWBbazMNzzDRrlRwgQdZmd1hA57O-pnZH_lBUr4MhgqYBKrGbmzMRhdCX1M3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaeAYWfwf2JVtHjmHpO3LY84_KqEAaPzlemjfBxHggxbmq4w3uueLJ-lzQNYxTiKmJ4zzofq6-qHbPShLeLwxQZi1fMRg4-mjbBGEfECJZRQW72qHNsIwdhJYPL6JgPlhbqUXyTUGNRufOqR25sQ5ZwX6lKEOY7_SIzQTlSYxTVlwqcD4LI7ONSPGs_tsTBySTZFDdJN-KqN4UxXl3TBi3N2zVQBWNo1nQf_j3nbybryuNGCxjiB9jpElLTVHho9k4SsAAV6sKSMrJRXub0AGxz8uwj05dniCn5UAD-tenzXl-EFpUjxKaCc2tFb-Hdh3YGMO8IvU3fIjlySxUACEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7u1IG1vimvHNdL3sjNOfSgmqgL4PJKqchcKd_EMfnifvR0evxHeIDLxsLCf-mYKD7JhJjmv8i8MUnmeVKbqaZHtkZt3blEYgEOJfr1921Hvsg8O7Ev8-oJI8qJoDgg7y-Jz6uXtP1dDTSIIJDGWcI5ZkVHjPw104nHj5uHJSPhyUcy1c9gJ9aaG5hjnqbDyyJyF1oSoJB7kaA41L-iNMBI8RltZ718nOia-b5FS3s7mp7hpH4KObHrtBX_Fccs8z64RdUJ6uXz2dbNQDjtebXtGbn2pjcJ9OQd_PG7fvdn9GtDGR6N_Qx6BYDJcwDyKlckGs4W8GE5BRbOlOm0jIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=MUIWQwTR6hzGqNRLV08eTv0mgqWOX93SxHcDEGMbFXFURmGqyNW9zY3f9DkThJp_N4I_0prJdeZyt0yMhGC-g9d0Dk0CXlXcbpyu9yE86ROr0645C2GSkYwyyxNhQ5dYwiuzgB9w3_ejVfSzlZ8171KaWUNrm8tiL4fw5mv813lR5wpVv_JRjAJczhA29t_BfmVAU-u6pG3DAPE8Zgr2W1AGIPebRDzg8mPqQS542JJ4Bs5b206Aqqbj6pMazBvxnN10VPD-sp_KpZcqs9gPyXbIt7n8j41QWn8iFiD5PmIe_blLdb_rqEMN3oQzv94d1FaPS02hgQCNNgBCEVWkZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=MUIWQwTR6hzGqNRLV08eTv0mgqWOX93SxHcDEGMbFXFURmGqyNW9zY3f9DkThJp_N4I_0prJdeZyt0yMhGC-g9d0Dk0CXlXcbpyu9yE86ROr0645C2GSkYwyyxNhQ5dYwiuzgB9w3_ejVfSzlZ8171KaWUNrm8tiL4fw5mv813lR5wpVv_JRjAJczhA29t_BfmVAU-u6pG3DAPE8Zgr2W1AGIPebRDzg8mPqQS542JJ4Bs5b206Aqqbj6pMazBvxnN10VPD-sp_KpZcqs9gPyXbIt7n8j41QWn8iFiD5PmIe_blLdb_rqEMN3oQzv94d1FaPS02hgQCNNgBCEVWkZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YsvMScNnpLNlS6x7k9jLc6PKAf5CPDIWR5_Uwg55bNq-WwD6o2CTF5rI_O0A0Lua42mc-abtgNu2WP5kp06ee_dZBnpAe-5fwTisyR-D0k5v32ykAqjZK-6h4zH224XpnWYGoTNFGmcyHBDeomLvapBoVLnvwvEsgbvarfmCTCvzfYuHsFCpsm3-NnK1pY0XkqZtpcZEkIqx1F2rG61R_BaZXlKRZPQ8pm-jX6dmfHviKOib_yThJ-qFG89UDWapdrvuj3oEmWcHF5CEHr1PRRYo_VUXTriUZxuwPe42iDvKAUT2qE3TTcvlyA7EXQzSb1rVevzZmtAVj_jc0MSBRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YsvMScNnpLNlS6x7k9jLc6PKAf5CPDIWR5_Uwg55bNq-WwD6o2CTF5rI_O0A0Lua42mc-abtgNu2WP5kp06ee_dZBnpAe-5fwTisyR-D0k5v32ykAqjZK-6h4zH224XpnWYGoTNFGmcyHBDeomLvapBoVLnvwvEsgbvarfmCTCvzfYuHsFCpsm3-NnK1pY0XkqZtpcZEkIqx1F2rG61R_BaZXlKRZPQ8pm-jX6dmfHviKOib_yThJ-qFG89UDWapdrvuj3oEmWcHF5CEHr1PRRYo_VUXTriUZxuwPe42iDvKAUT2qE3TTcvlyA7EXQzSb1rVevzZmtAVj_jc0MSBRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNia0IG6b6kfGPDKSopEMgXiI15oRBKr0tctjJeyun8eVxbFZp1ysHaHWNeLM6W8OmjOCREPmFYAnXgKs4VH8OJFF8IPDNyTkR_hlxKb76JV2d7hT50mW4wSD38ODLwPLDGf9qWTCNg5jdlWxVTmLDgtdzjMvvc7b8M9B4iBKeYEgu--epsjOuRBcf0rFPRk7ghgbVDmpmEHqG9VYj4l5tqFhsOw9wnMuMsMcEpaTkPHCLL6yrUhgB3pTt8nd_W0okvCollHrEY1MlCx_35hYOWtK4aLx0OrkX4LPjKlvnohoNDwPYIYkOmgvTynMkmvqywv3PCJYlE5UDAYcVMK6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awBocgA0kJD5kDlkfISZTwAeMoCv_uehDCMzsZJuRvuxLA5kVsmrFAlLNauSS0eJEJgZ3qDYpbHg21NH0RKxB7LLTA1vAGLYEejoQswfg5Di609sXqrvPgmgVjNqqTWVhglP3LiCLYp3VgONY49fJkePTlwrnzQ2MF-dWAcpEHcdXczUuT8hmz8d_dwI2rfMGrPgjNdeu5Xr5J99XoCmxpw_TQ-GxzPTh-8yO5989_lctqpz0YrQlHvDsKU0_0mMuOQK3x7RVJXOE8nc7uHtBiOwShV7eUFya-T3RPQ77Ppzp2LJ--MM1tgV5KhM5Gd6XTSCWgsMizRLVq0sVRLsnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEFmhOFB-ytHSLkK7lJajklsXRURtprYBIKcmhBwAYTk3YlvpG9-NeJAGK8C4xuzMzwxUnTuXiORSOGbxovQ7LXNaLbnScz0WBZoeQnZvFtex86gyMGV4CePLg8F1D_Blgn0zfBGAUlKXVDSp9BYRPCnp4_8UCr6YDlXnoe-aWVCtZ4Up9Grpam2nwqhsYrazF9DGZaHVxcl-hz-1fHwlu9S67pSeZTP32XlPkRmdV332nDlszgxEq18WJK5m2tdvMf2KzQM8Cn4LFYuhjU0j2cH0X4hzjl62Y4eYoIbgvNad6G_QL7yb3Nw8hmOeBGzmZpY4JgQ5GZLGWjroZMJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ityphXUg4fxm0oIsa1SU5IP3PhjMUAHSaUs7Q4LYYKy6pPgmY82cxr2pCjtWwwyy75hK6CvdkJtqrfvC4HD96qFrWEHf5mwA37w7AVvPcMPaQUptbkGtybQkTXtgL_-iuPBnEG5tMitSBy_-eM8jrR9aeoHqhySDgABQ09k36WgYCiOPUXUyQgKSTSuNEtE7yo4qwsuAiWnBapjzKV7rJWvxsiD5_OvbPCdUEwjr4KjKWwbTDZABKojuJhAPY07ECGccone3D6ToWJBdTnZe78g6Y6sQwq824n4U26VCiHWr3vUjVyqDx12vbm84U4q3K1aw1pw4XOXANz2ryJSU9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4XiQXeqVlq5B45XvwTl0oDWJRaPWOd5gyU0pXxLKUczihh4SwwRZqjNvjpMoH4n1Vw4nlntuCKVqxG7Ntx7SC6nI3GEtCuogHNa6jXVQgxHujHbASAxaBgD8JqXk9t1TNIt7yy4E_yriSNmKHA6oZNrOAeF7ztnXMhSoeUt44d9tib-IUK62KSGnaSp0ocre4P1mb2qPqcjy5cB4L4Z6o90LjWMV53Ep3tIipCFB01VB5OnuB-JlkOKTStdWC2-O7ibqrjmtO-fP-MkEej-xurJF30W-gO1EVWXJWG2Dqy4ydtt-Sc7zuy0npuV5qss5RG5cZP3Dw7jO_maq0qylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzfH39HOAhdbJL2_WP3REVGzncdnGZbuGKD6SrFesv-AttqQIZdDPGvX6UMQskIXLiSQe-t7WxvVCTdGibSifjiRa2UHEHp_NR56ZGe6koe2JJxWH_ng50GEjEDEArA7_LhKJGTC8hK7o-2VrK0Ah2ZmhccHCEwmbpbam6CQUQlj5VoFzPv6F8FLC234PpUdFv5Ss80fmT058zsPkJ7zNBaiTNodwaVWJ8eWYbS5orS4um1qZF08lsZPOtvkQMbh2t9s9f2X6z5dtBgfO2jKi_GFX_59pRlSM23hBdYqBymF1NZpge11lwGCB28ic8xP5xdZShNDxCepzNCbnYagCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPYhC8eJ4w-Edyn9DJrm2_eGjINU9h60AFFBUMpy0bfYmH1JDvJPtLdlnNzmKRTYuwVvlIqkplz3UF83ij8EclpZoSnEqhN-OAvbyOZQRqvaP6r7Cc2CYTU0kSpYOUADhfHm7WReKafg-uGeYAx1xx2djXManEzflMPNckLmpYO2Ezti3EiksGwQptWV16m6XP6Y1qdHIhvC11G5OcSasCl0NjNIyeeNqx9R8M5KSunxABm0MWUT6KIOIfJq6J6XQdcpD0mOartN7rWUwozEhxJlQq8_9hlhJ3d7HZbL0QpHyXJoOCoQqCTdyvevnoOkoEC5RMTY9xeWjJAX1CVGxg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=RgkR2sXuktc_9K4Hl1RQIcKkctyKF2cLTXsd7mWkloTXJEjn1MQwYStGTgbUPRLz-bWYGK7W8dHYxdIz8pNzprqmEjTebr8J4Uv4s5vop8ZUMLyBWdQtcYgNOyLn3wTX68RTtx4YtN-H_G_c4jzHlHHZq8CS13H3zYlMCdQaByptAiD0V40idYFVUYYu8ln_uvpzuD70tfzSwEoTcc1kAQMy853IlGB06MeRFVelbo6JNLMHquLfqVHQJHQKN2ipxAoPL99X1IZN8GaQlgta_fNy6mjGL5adWegee8xHm7cnR7PryMlmBhs3lbiKtq8xb5qgY1wblQhBUuqpNuS28Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=RgkR2sXuktc_9K4Hl1RQIcKkctyKF2cLTXsd7mWkloTXJEjn1MQwYStGTgbUPRLz-bWYGK7W8dHYxdIz8pNzprqmEjTebr8J4Uv4s5vop8ZUMLyBWdQtcYgNOyLn3wTX68RTtx4YtN-H_G_c4jzHlHHZq8CS13H3zYlMCdQaByptAiD0V40idYFVUYYu8ln_uvpzuD70tfzSwEoTcc1kAQMy853IlGB06MeRFVelbo6JNLMHquLfqVHQJHQKN2ipxAoPL99X1IZN8GaQlgta_fNy6mjGL5adWegee8xHm7cnR7PryMlmBhs3lbiKtq8xb5qgY1wblQhBUuqpNuS28Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDQ3ygSgSElwI8s-LL5Q4FiffzFdwKaERftZLADA4AjksuayzdGc1xDUFkwFPAvYEBJb85ITfgykxWOuyi5I4qEnMVctbyDk2fy8kLbU_-iINXePHidXFQzAVg20Ax4i3lKBzmoME9z20mkHNqBzdxxHMdeXK8J4FxG1-wQabjl5VtdEbE3uGRC-kGj2wocIeiofefqZYDXAlAP6Djfh-6LgdMlMn3QKE9buiBLVYdOIlBE-nctwdJKR3jdDOOL4xdgK0blGSmA8tX9j9yyYGmINJO7i0HKLe2rUrZVreSjXe_RNeGUPlV-DLHuC2TnJ32VFwP-MuxgDTHY6vZosWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=JIHIoGCWrTRJ6_dGFoFz0wadeu6F_uzQyqq4x765Db4xk_1HnaYLn5G4LVAJ-XXdxk4degPtuTUMP4SojwLA5BHjwJRgQ47ZdoPSPToTJPN8jregeetG_L4d08fbd1Zza0tvUH5h01GgMChGZ61nmAKPkb3y61olb82S0KRWRO_h6-fHqSinWrPa8FX0nUxAdV03Ltf_DTvb69_gf9pg-ait1fN0GdFi38t8cLoqgYpYxBcA3qi7I4YDajFClvIEhPfiQbgskoosoOqdECl8AJUD7MSUOJUlXw_7SiQ3Fcl_Ckfr5NrUdUjgAMTB0TOS2ly9Iqh8ycS1WmBbwDx_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=JIHIoGCWrTRJ6_dGFoFz0wadeu6F_uzQyqq4x765Db4xk_1HnaYLn5G4LVAJ-XXdxk4degPtuTUMP4SojwLA5BHjwJRgQ47ZdoPSPToTJPN8jregeetG_L4d08fbd1Zza0tvUH5h01GgMChGZ61nmAKPkb3y61olb82S0KRWRO_h6-fHqSinWrPa8FX0nUxAdV03Ltf_DTvb69_gf9pg-ait1fN0GdFi38t8cLoqgYpYxBcA3qi7I4YDajFClvIEhPfiQbgskoosoOqdECl8AJUD7MSUOJUlXw_7SiQ3Fcl_Ckfr5NrUdUjgAMTB0TOS2ly9Iqh8ycS1WmBbwDx_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=besaxmf2pNmyDP_s2lQm0IyeyyyvpE52KZvmrH_ES3ke2ucNL-1m3PAyLm8ZzkeBPvWzWjXGS5u3-bo0C74arbcDTy3s-mFhAOe_NsFbNXgF4dWFBGZNV-rPFOV2QrQn9jhjxThI2fxecnztT-XFMeOHejqw28Q46m5V5vDcKUXg83V_9mTSaN_I_1M1qB_Xwa7RX1FXUB-rcD4DFAVvdxQzWMg3na3wa_bFUOQ6dFNayGl5gScxYYux4CxgWgfYHnRxl9pqWoRaTqtNBJp91BdLa4IyTNEsQCj_XUT664Gh6yrJGhMdAkrdZNuOiTlZFIKP4wLRKwnLo1RPIUw5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=besaxmf2pNmyDP_s2lQm0IyeyyyvpE52KZvmrH_ES3ke2ucNL-1m3PAyLm8ZzkeBPvWzWjXGS5u3-bo0C74arbcDTy3s-mFhAOe_NsFbNXgF4dWFBGZNV-rPFOV2QrQn9jhjxThI2fxecnztT-XFMeOHejqw28Q46m5V5vDcKUXg83V_9mTSaN_I_1M1qB_Xwa7RX1FXUB-rcD4DFAVvdxQzWMg3na3wa_bFUOQ6dFNayGl5gScxYYux4CxgWgfYHnRxl9pqWoRaTqtNBJp91BdLa4IyTNEsQCj_XUT664Gh6yrJGhMdAkrdZNuOiTlZFIKP4wLRKwnLo1RPIUw5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7E4qZ9LlfmP-mTymptTnfB0QOnZT7eXoNj5sDYgp2ukV6J3PfYP2zqkka-r1-2co5LVQDsZEc3-q3bGLsqv7Ib2TTADtSquaNhyRYSutJHQE5E5E_GpSXTnapcNB3Skj8y6Aij2E72-ZKa0tI0NUZC0gJAdJLyKIBuxVBJ2N8GZoSTy3P4a6Jgu-_Itn9WitsNEYQ8sWemCxFljJPDrefef0bj9-9Z-IKdPg3_dzu7xv-FshgBZfcdyqOFccVCVTTn4yKaYji7LnCQe8n-F7NEyaShjzV8bzRxqwoWcTisETXUFNDGpVKDAVBcGuNUY25fYG3IajsbVWh9QzD_mwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3_mYsnG4MHqAZB8wwbtyC0hwv4xU2mWdvGPF7OGmUsjMhpIUEPlVBj36xLE96i8vAcNapMJwen9RJgggvJjcnQ6RJ7ckvJKiFx0PxIx_JNCNs6Cjb7KkzULiTuhubdUyvPUn5ABYiV4frP8BzJRS4lkVRXliWy5lobOmBkxZiJYQQEqZX50jknOA42VwNR4zKKoBqNhkDaY_1PRuTdhQmui1RndJoNmZ0fTyxxuzn3yQAAmex1mpB1L77sHP1QeZ1yfvEemh250dNE2dwPKg1XV7RbTz7uGxWUaScTxIFtNtL55Xo5UWFnfnObmOFuLUYupQu9z9l4IBBfWUCaQHQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=BkGLtpL37HO0FpKSj2EMRSgccnafDFZaj0W-ZWVF-XFfjnjXM200Wm6kjwynfUpLvfSwQYcSFUNxzrKW4lXkBBD4QsKtsUknkcgLB_4es2nN_Ng05xKtq0E9_fi0hlBa0DCAPsCriRUSxDCu6AshlDC8TrPwS2Fh6okN0L5bnHdBz7YP46xXV6G2kfb4ztptgTvZRgNJJdVlBl35lDDU_ytOv6X2i6xrp80_brXSBxtZvuUGF-3qt7zJue3L-xkoNxkqBRbIBZKwpxpGCSDiexXoIw6rJJlecgaTDezYmLUPQ7r_dKd86xVhbrAqzakl-fa2NkkyBYfFniS9lq79ZCN4u_gkfvq8xH2Qk6y9Vxe8zIDvROXBbtaDCXcSBhnGzPt1xmdHcUCY5NvVm72pVSOOKctFgyQvSyOFFdtXZg0r0aQTIdguNvATpcAtqk0PiAQ_P5WiIwm1S4V_KQGdOMjE5Q-_CUCGNrJ4qohPnvACeMqrGfWeX5awFlZJz1-r0Iv1v3kiqiBF9CevusEaQw5Tkv4Cp1VA51qnDvnU1tIrUbO2RQeKW7aM0-MdMRPEnRNI4d9fImNTtaIZvjp8rF4F8RaEZQBE7oWuNU9NXFnLc3rqNd3truldO21clkiElBQ1uFdOWUPa61esYfbN1ORefSuYZlq_vy065CQVm2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=BkGLtpL37HO0FpKSj2EMRSgccnafDFZaj0W-ZWVF-XFfjnjXM200Wm6kjwynfUpLvfSwQYcSFUNxzrKW4lXkBBD4QsKtsUknkcgLB_4es2nN_Ng05xKtq0E9_fi0hlBa0DCAPsCriRUSxDCu6AshlDC8TrPwS2Fh6okN0L5bnHdBz7YP46xXV6G2kfb4ztptgTvZRgNJJdVlBl35lDDU_ytOv6X2i6xrp80_brXSBxtZvuUGF-3qt7zJue3L-xkoNxkqBRbIBZKwpxpGCSDiexXoIw6rJJlecgaTDezYmLUPQ7r_dKd86xVhbrAqzakl-fa2NkkyBYfFniS9lq79ZCN4u_gkfvq8xH2Qk6y9Vxe8zIDvROXBbtaDCXcSBhnGzPt1xmdHcUCY5NvVm72pVSOOKctFgyQvSyOFFdtXZg0r0aQTIdguNvATpcAtqk0PiAQ_P5WiIwm1S4V_KQGdOMjE5Q-_CUCGNrJ4qohPnvACeMqrGfWeX5awFlZJz1-r0Iv1v3kiqiBF9CevusEaQw5Tkv4Cp1VA51qnDvnU1tIrUbO2RQeKW7aM0-MdMRPEnRNI4d9fImNTtaIZvjp8rF4F8RaEZQBE7oWuNU9NXFnLc3rqNd3truldO21clkiElBQ1uFdOWUPa61esYfbN1ORefSuYZlq_vy065CQVm2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k15kbou4KOxgSx6B9MVvteOtF-vpAAjhNnv8ufUkz0bXLhG4Tn9GgT7cU72naqJX3guBc5HWAtSSE-u7xPm-dxxuuf24C6KIcuLMGrMg22UmBB4-K7-8bwFJh0rc0jaohePfCNwEKPHy1UBNvSKTituXNEd2_XK0IIXO2preGNWRNU20gQr4lhyig-nzft7qmivdezSF7nqatECER6xYoCixT0i44HAecupjePKZxg2iAylOhBuh0eMvd8byB7PsyVNpAzdopl5W7TptBcMrUE_bNZrBLE_dAvKp8-9LOCk5sV6Iqds46XbMRs0x2xnrVZFbrtpLaO6f84EKW_leiA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=WjhkCuf4DKfFTfDdodh6V4KWbueWU-R2SX9Kd5cen0Oslg96tDScpjgD_4dH6QtoWnRvfdbfE9OnPJiGOi-bwxN96eMIZCwXOkKFV-8lBdOxmgDbnz0IPl6DYjnaj08-gfVhknkXMBpou_taY54mdV3murlEwNh_XCDmMaCOTeQ1B7CcfanTLyxZe4d4Nxg8yuUCFckRgAzeAkQ6f6mLFZZd9njkJWSE5QXimhMEYChukoAza1RADo5D-f24elsKq4cPsjHkPEdHHT62rzlPphca9hNhQI3frRfGgmiIyqB81222Tz8N-sEZUWaxus_hks4BtnNaHpj9xq7akWPKPogiWx-mwAYCWInwrYPBH60Nh201zY-K9o4BsnlVV8XlhccbYI0f0sp1L_ktcl00i7HWo9Ojs7G8e85XE9mgF47hayjjkQdrXQ-mt9GnZGRwfNFHQlZ447lHXeedDt5Gd5-eSLhoQMkXy0XR-hX5zkVdFJsnQECpeLekp3-S1oRFu0QY-nTGq4CIIVoSgp4ZHcM5cOLLSPuTRwrdfnltt7zC2Q1thrPZ0EG_sishVOdJnf2a0E1lnuNCoQi66QUNnJcsL0Ssk-BU3bhc7gR0Ifg3KyeXP-CnpPw_aU8AjU0GHnGEk-t6PZ5qXI6zh4WUmgAvAb7JldjLzxtIOsuqZjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=WjhkCuf4DKfFTfDdodh6V4KWbueWU-R2SX9Kd5cen0Oslg96tDScpjgD_4dH6QtoWnRvfdbfE9OnPJiGOi-bwxN96eMIZCwXOkKFV-8lBdOxmgDbnz0IPl6DYjnaj08-gfVhknkXMBpou_taY54mdV3murlEwNh_XCDmMaCOTeQ1B7CcfanTLyxZe4d4Nxg8yuUCFckRgAzeAkQ6f6mLFZZd9njkJWSE5QXimhMEYChukoAza1RADo5D-f24elsKq4cPsjHkPEdHHT62rzlPphca9hNhQI3frRfGgmiIyqB81222Tz8N-sEZUWaxus_hks4BtnNaHpj9xq7akWPKPogiWx-mwAYCWInwrYPBH60Nh201zY-K9o4BsnlVV8XlhccbYI0f0sp1L_ktcl00i7HWo9Ojs7G8e85XE9mgF47hayjjkQdrXQ-mt9GnZGRwfNFHQlZ447lHXeedDt5Gd5-eSLhoQMkXy0XR-hX5zkVdFJsnQECpeLekp3-S1oRFu0QY-nTGq4CIIVoSgp4ZHcM5cOLLSPuTRwrdfnltt7zC2Q1thrPZ0EG_sishVOdJnf2a0E1lnuNCoQi66QUNnJcsL0Ssk-BU3bhc7gR0Ifg3KyeXP-CnpPw_aU8AjU0GHnGEk-t6PZ5qXI6zh4WUmgAvAb7JldjLzxtIOsuqZjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpVM-uHWgiTb76dCGv7S-tyBQyoBxrXFwqi51QdWYJz26aCe9zX2icU3oxyGMSFdlIe-z9koVoQzNSwwO6qjmLyYvilHOYdVI-td_tNLcwkBcDSv-5voldAuHObzLWIW2m0prNSIt09PxQ_DxQyPqu1mKJevjrK09mhJyOFH7FNsMJXB9XbNiEIOr1Qg4u2Qbjzg0kg5ETYxST1ZuzXHE7ht3moyAI2_OQM3bxUYx_SU6Pm0mnRRhvQsztJmz8Fe3cKWO4wTPrxeKJohGpUeQauUdHTVACUTrrDKvFPb6pYaNmWH5fIKoRmEYkQHOrzK2BSM_xJJUVHaasYTPjMaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzYMWMmQuY6Su3OXdm2PbD3R6J07W2lUZ0DChUKgi8o7I1cBl_FL96FZJKH4UmMpDxZWBR2741cZQ-2jykOVAe-kJl-vTsnfVgHTDxCvWlwck1dBWCdOEXrlN1tk9AU-LxvfuN3ILeZBFs94ORgwtlj6ws3swHEIQuOHpyP6FV35WDQh6Yyc5SpQTXWVaCkG5GAGRoFKPqWoWMsc_AClaAFHbl219MLBoCyK_KG1EMF8LlImO1JMbyQME7cOcHK93fkgVM2-K_ySM5iu0UKyV60n9CopPVhBogaqOZx1RWdYluqqQIxeuAoAnZOLrfbaXOo9GN-n9icAhR2_BA4C3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6Vb0RXov-r-5zJxJZpfuBYWy4Fa42Ff1fIvaUxc-msh6_FmFigJPQYHvfP5QtoVZynyP8JnzLzcp25W0xYU7Li_vxRZlte5qRtBN1N9uTmFRoC4Znzy4mg3gz1mfkenslminLStfTiw6wSvIiZxX2O203XWz6pmj8WEkAe7D6uVer2obxLmFq6rswQaHE0EeEajKAPCgvQC90ZvLP8cblLVV_De9BfWEl08fUs77DB4RpO1dQYhGcl0m9EIjXyV_tDLIW1uK3oEmJpwYooVYvro0i4re9590LZU8AHetnOt6tKM9yDCb0wYenHOZIzfcMWUB1dJZFeA0VTeeIiDYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhwWUm6tdIwEDlxsBeWsO_Jil5tLzLJu2iIItj6WrdyaVMyh-_emsoAKCfxD3LOr5bcFtiz3af5ab8xCNAEzS5AqAmc4llNlx_QNY-LgTToJj5NyA4P8S1OrK0SR3LMlnA1lq1t5hMCj994rLTZ1GLjEd1Vc_jdYbwt1Wy5qzIiI5Ou5605pqgRjQHecakJBN73okIvUBfCPSe5aLNPplE2xogGLbQhsZxipBIvck9hBYj0YPuTPC6nbxWvaccKkjStuH0D83xarrFUHZiK0GxJVWj0zLj3KmcEy8zDKV4mtPNsoezef8u1IOWVajmQnH0CbRagMt1U4VbXGPepLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leuGVlKWZv7j18NoG-vJ5lKfkQAMdfwNVO4Z7kc8JT47t2wazCi041xBJfDTYxMyu0AAIgbv6GL1itMWEzCagVrG1LTx5TRfw8V3AAuhCRyuUPTWF4kgId9CFWKa_SLFM-OwcpiKhOVfBf1pBFgIgQ_DgAKOKnxOCdJmQZcGqQ_1fd8ACdRztz7BUWHgn32-ejtdISh7G1ceLr2QYeRkwFOFFs-xFyOPwtrbaZAwpcFBdDzXOUufEDR1lk8TEFmqKh9MzlO3qDsSSiL3uLP9YXbDGNlfKtyeR-zO-ACGCt-NGlotGP-1qqxnW9VAq-xParJArJMh_C8q-LP7TWkXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJH3YFvdyi-pCkUZt17sS6AP2EolYLfBqeJgCOco5azjF-HUkcnSy7mlKmG69Aex7Sm9LiThpc1T-ti3BZMhM8iuxU_AbTjrEwpC5w4RTnJn5aUTME2cKoDHns7eu2oBgrp8mu7219o_9ZVNoZtUBWGdR47ptIUdOgqlIFwwy6hWb73gyMpoEVoZoxEMxNjNUgIjd8id83VJhx1ETgKXQLT6XyZz26W9WW0iBV9jXF4wKh68fKccuhh_Lsa8S4pz4cZMKF-nVtFhbp6Yynj6bL7_y4HNkddiA9IdF73uHA2wldpCB0VwDMO5zPeRz_2u38xAzMrfeN6Q8YMIODPxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGgP9b52RfxohqBgar__JPosqhlvSJ92qsk6y4b9SaPgnC1jQME6I_Y5IW1GZO79SlhoTdbu_qVLx6KF6sPkNfM8tPnDJs-BN3XKLDxTT53vTlDoz5FpSNHx5f-kMgFoLzQxrL00a-tRMMMS2XLLZxim98blWNbZwoA8buEyeeNpg2qu515Ycq0zqaJ_rogxPFdVpBxpUELp7tdmT_oFukHXy3SOW_NrmdnJEdRNmPUGajI8U8_NEe4RGZHmPhQuxaOpwqwB9D067R6jcFjK339GBmzyj9jiPQvY20aC1RlarqRBNEDsnsfANG-C8CrFy0cwT916SAHAI6ml7czKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bqb7stDJg5LQsddm3LUqKGMgZGPRSIYBYpQ4nMRIMQVWc8bbaDSN-NCCCQ-7KVM4mmu_4Vu21zuwFAMQs9_idBqgdItx0jpH1Hn67MNNjI8wqKmLvqnq306Itct3iaNdm7gaB8O0TKiGKR7G_M-aebdvgSF66zlFwnF4lNML3Ev_6Pv8xUY1G3z-Jb6HfPPhXlUrltyZM5BF_M_eCBzXP4oKg2Q1btFbz6Bpc0BedtCotOtsk4GWeh-l1vVsMShqLks98UePkTLglhe_KEXPPnbeo76KAvq-FPtaS9Wx_CQcyOig8vFCHMndtcZ0Zgk6ZWZ70AjJjEm1cpMZODPomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGESh9dfTWYaNmCqCdh7WN0zmeSWJ0QBVb5oIDI22rRFehRg25pvqQKRYJaAtCWyBXfUKNd9ZNqX4rYerJUvdSKVCFqoxC6662jRU3xc3QAIM7dk8SrZXd1U9YUK7wPK6USrFKMlcFE2rkRn_TmKZD5wOpseLiw57lNB5OAX0hsSNGuVRFjOD5owD180lT8Ea4dTaIsxKIIZzb7JvHRIlZaZGOzKlJ0rDZo17pz3r0A5aNjyfCzmmHgU6YnWFeTa56NwyLHZC8GV71r2WPnIhSwPwzpo5YBWFot0HfxMaadFlMTdsEt7SQKtSORz7DZVnnGYiFbzzE_NFXIeDMuL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mh471ZYlbUFu0vMQviD_UkJAvO7lC5xIvm1_N42qmDVLo1FuFM-I3IMoC3bhxprMejEl-OTC_KCpD1bEyuZ2hzIpn2tdp_BrpSlV5mLMOdhtLoeWl5GSP4wAVBwSkStnELNjmiphJmGcKEriuqh_auyit2qP4mhB9NztvO6RJFe7j-CfZ5LAlc03ptxL6GpJESnLDUp0utuTQ2I3n3bjZufaYHBOrfi3h4zk47kVw2ebfPkxVw7f4UE4zloYlMQpj1TataaXV8cjonEIkz-DBQS8ZeaUACS0Uu3-6uJpgvMSN1wY981CXVcS1N9pqRFHGBHErByN0RHS72AOPK-0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MejNl1HwFVPEtqh6R7NlDzFECgL86sPNyVG-BJs4H-H2DZgHJZjaJ1I9n_MAFEUSHSsrFIMRa5HXf5REzD_8BvStuHjqzp7plQvojIQyWKvfBZzutg7qddnbJfZGpM3RfeQl0z4QhewDE-nxHm2OX1Lrl70golYpaR8EWDNPxpZaA743FSKw0t3tKwrKsflUKpKnw_oRjRyXiaTuV0HpxCDe1_E4cOHr4Jp1Lz-D8LgJseDdtOM64f2Zv1jc1R4oFFq7GIvQ5hFZ0wfCD9l7YvNyQrQDZjI61NxhD5kVxGZfeLNbibknG5v4flkJ1Rz2i4h4zMK1CuYoJW2NNTV9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hubpeopcTpCe0Hcw5_MjiMLTVqm7LgmhUNOL0Ia1rq_TPltBz_vOcvsDWPQklakzkFaYbeCAibnYEnKJy2O798e1Jle5iWZ2oHgogH8TBFCo5dQ1ilb-ar0XCcgEWmNZs1c7ha4YN4vuCLr8lSmkX9X4o-G5d3TfM9MZSmPGfUJLaStpD38JpQzawUWrxjb-dbVtAzc8yj2e-ahToDnuFZjksZlCZ_nIcrtA6GBxSYWnXhwurQ8A4QPaMxuHJ-N5qFplSzXBXIlqDPKecT8eT66We4neBeGKXaiXVSbOn0X6MdF8K3C7IeiyXZZz9_XjKkkY9hWkrnGvb2r_H2T6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwBvyUxJz8-aRFGkqt7UM_19ftWMGYH8oUeCo8e2noiKuFNZaH7DM6hOLzerSeUsoXRyqqrmBh31BrhkQaqT74_ldSMSU7IC6EVMUljAp8pAvHzKMgH9MNMVgSZ_EYAhULPOazkhJcJsuwZwR-MQDDYHnDnXUCmFf0q-y0RNVgFiya4VsApPzwWA5NgKyOX8FS20louTjwDkMFK5nCiTv4-R8BofQ2b0UItSYnXwvIKO_2AEuVGHbh3-ts1sN71HyquUF1G-jU2TzwnH7avzixH9MqA8InPLLFVAej4U4h2hLQt3vUBDmqq4oVz8ZJbzM818_Gg0pyM8jMuFseK5kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjcYdHnJWEj9cTf5Eq10yKEBswcvuf2yWXHUtIpJoOGrBm4OswKjjRdS43Yf1ruf_Ezk1S7CrYlnCvcT9jTH_EiumQWYQRht8eVzDuBUm8GHfWuI03X0cZnCbUi5ot6iAL3_Ckyx74ERPTCdOcA3skAcqirJodV6qLYXZ9ljraQL-P2juC0kYW5LUcBAsSUR26F_lQtTi0rk_SKuP056LvcUUvIehzBvXHCa74SThtmCazxfWfL9Jntvyant3nLrbAt5vpAR6fYVamfy5Mlf42YL11TDDNaJ9Y0_7yvwYW3OVa86sMwh5M96wG04lv1AmtmdnZKSHtkyKQ2xnGHb1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI2-4Fq1o3Op3r9oxItyXeqpgnFwQbg3sVFazLgKdBXddQZu02sZSQWxI5dt9uEa07gV-Vk9ks9ZZTS03XdmkJ9rwcoJ2S-bdirPPkmQGUdxrY2m8tjM0vGBMK4PolxjKTWmk9xLyV9Qt9JJgIUVpmDVJYLAdfhmXN69is7I9lDiqHXSY6xbt-PaZmTihfB2paioF897t4eCtFdTEm9OqepV3g_94KkluGZqVX2USWmj1sPy2wM2PPfUMY9vtu85nHqRHhLlG0NNq5vwLKEMAMjDExQP2cSA_Nqv5TermcTUIvjcVPaZvsZAX_aA8beVBv-L77EteBwqhrX4Ccofiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4Xoot8dfrVdXMOvAOSy3C6REZjF_Kym74IN7x4k61IPIvSU26rZlRqrpq5jaGHPXoLOyatDYwdhLoHmG1Q5d5IakPJEJmKgWT6dArpzdme_gNv4ZhPOZhyapBy77lZLAQbYtivEHL3qAcWXfmiDLSJCinXUb6-Pt54mRBSOURFE3XUfeCdsBpGuUoP_-Ok7fIBjuBK-HZkfcLu1ne9GvBgH8MV_apk-CuWQ5ni_9Jet_ndeb8BBiFrix4GKWnCigwDKxfI_BTraMLT3ID1-xxn0uGj3BhyoudZBqocN3kYjXee1fr83zZbzzQiRBKtumFDqfukMSKP5-UlL1aqofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WoQI2lnmXLySFgxiKcvASNu6kjNpQn7SqDsATyW0NOCLUo7_AoVVNykrcv3SPmSRsGBT6PAJHHrq4_f4X_ygEffGByGltW76zC8PO2hCctydP_Z5KDWzNN-OXmhT2yMC62aFbEt_WQEBYJS7jaVsknWp3-C5xDP9jIfJQs4FZ_VEfj531-2-QtEo56f5krj4mQTw_9m3LR7bDGBvSlvUL0KaHmRAQ79m5KD1Z2UO8FKbG4eZFTQ2ySy7LagfsTee16y7yNqYy8VZQnXU5MH0wUu6c6qYOQ-FlWeEDBBCZuT5ZEi2lZRWubwfWoFKfv8PnLUlenJWpYHrp9RUzQkTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q16YJ3A5r0y21uDbmVhJkHaISCHJwW01dXlmQ5cdLv_dzL6_9zz-J3RPUqhXOoX-SJsI3EvyNVj85KsYSnpZwaFuy6eTyJYt6Pa8EZQ1M9ZN3HdCrj02MmDAKmQAMn38RPzgoH5jCzKwAT8nIjnAD-K7NLZ2DlMVivGMDpCnfVytkUZDPwW7RaKNGVI68ntlJP9xhPRlS8ovtDMYVnYfYJ22LeBBnTByzn5_R-SQWxiZXk45Oeu0POqO6Sg3q05UyntjJL3u2Vs8kLSa61LtuP_Sf9zdgTUQlr7pSkMhDvfBBWtzXpumfxuj99VtGDTFjBzZz3y2S1vFxIQn-6WgIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HToMLPYTTi_DmMVfwbM_rhT776ziAY9DPLXhXFwDglAieHs6MoHDCYwjzvqkZTKEEDI42w4eK4YqAHmhf9seeGrVJcqX5cPxcvHuNYzGQRpUzZybkKY5dpdRmgTYXVxTJYVjmfXoutY9ASiFDEruTjlRhyZl8xdWvezXFz_y_JQV_JxuW3rACNQcO3JnRVqZtL7tfDdLa5h2WXQmKGN48rhsFMDkU0tN9Fhkj0j1Yyih2Eoka2tBQSCyoh9yIl4jxPr8jdn8MHWWGcgmwpQ68xkbe0RSSVLayJLLQtYDIcfsXg41ZFRFbfTwenKJVlSNDx_hR7DcGTtdah-_3zd6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3fCDds6HeKS66vKWCxatZwYKIHKYKNQm0FiByJ6GoM8vnTXpn5AL2SBSQd3qHMK6vYo6KVwk0nWIHVDkA_0wBBDbPtYx4G0q85jEqcvDZUbS2j0QowQn559s31CblIC9MwYZN308VJGB1-sIVqar54rORDaieOBru-R0yPlvltgLP06jVBMN9yjyNUiyhSjBY4tD2IFa6hDFBVsdbFF94bwI5mQQYPbeU4_IQhv2nxJJRnE27XC_jUHkE8b9t6yOEANKsJmAo5kiYzS46M_me4Mu3UNMdwpGLaglhIuntOx8jMZcAF5zqLDboij3fmMIWY0aB4YPVNpd6l7wzoudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVXjCZdsUMZPRc170d5v96HNpqYtGYOOX3qMozu71QoOZ2Pa7_BNIi4T0-MUCDbs01bdUBn_q4UjEyS8GsMpH7VeWk32OFLP8uMeyebNOawfU8wKN8SiPX4_yjeINxpsSqT-Mg2a6kpHlDg-lABaZauDFJVtHORXnMZQOrA_wk8q1yVV3ZrPl_LORXgJQ8CJO7u-hrIi6i_8cjZfLNhyk_aaWEBV_SFdRhqx4g2hjToqQPZvA_beeD9f62svuUX6UvsiojRrAlSNsrZIBMPksvz_fyrHPxbkjBML7njwjTPL7goE_cqXGAzWRF1gd5Ao5fDrStrvpStpRumTLdyMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPlR5DSSKRBtyNyj4hduGEUoSkdfRNwpnzs7JRD0XQJ1LFEB7EhkZmMdL8fBKYhHqe4aqnN84e7_ve0pvT_OyG1RTtTxonIt5k1SXSRo_WYBmfXmxs9JTYQUk0Xea9iO63JMLR8KvwDUMGHZvaXDNztrSwKtvx73EDv0uF7AUcJqlRK8eDCjiz7Wiq-_MgOXkqWX2kt01VnQeeNWy7i716aiyhe1Rof0_ptxV0s5nBOnLcPyt31LKtA6xW7ziauyjcILyjLoaC9IEgtxAkA011uCUy9U26g-7yCuh3bjMAB_JHwKzVa1MbKbij_xDI1xIv3rx7Kk4RuhHIFqJi1dRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1AJ65qT9yThzW0Ak2ZChPVR3RfG89N_JQ1kaJm4LceHrsDKD7SPa88qoa6IEp2nQVx09m1J0WAnNIAqkF0lJteOBvK-eEGknecXwOei_sXiwhX34KJ8HNyThPpJO0EQQSgQwyqmYhuEXUpJvJX0WnUIJ31Re4UcJszImpd9ErCsu_GqltDLIl32um-Nkv1Rj4vp3FwxV4WQ5LlM4bdRUi66oiVTr4EZiXtBw2cW0tsrTxyDfIxzfmFfXtEjSnZRl3Fa2jWztxvXy_IxjrX0LOyLBfBX4abLk00GUd0Nls21vtD1QH790Cox_3OAeKwSuZZM2DG1Ik2doGuAO1XbUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7x3NikvmXD1PeBV-MyJ5214ApUs4shkng5lldz4ThMpsu90VyBRgMI1gAm6ASEt_3qDOJKUi4KLBocH7BkzIv4_3oU5ZCDaOJnSsc5vIezD82l9_s3ufcEbCzc4Jygwkne2sZi_Nax6hTGTN1Bk2ejsGqgcIo56fQDPnLi5Rxc8wOxmFhCLUW_TDPs2qEzUlImKRKrqGSnfcFISYzQhyoSs_3ef1458SinrQV8H0gGMk2UuvGg9ihAkEwRQFpqiXsJ-oPbeLg95ObddQzH0OINMykDfgyqS7_sJTCzWVTQVIZjeHxTzEKoj0b1E3VC80I_VUrYssEj7Tenj6JRUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqDHgT4HpPkwSMEZ9F0_TLReZvyl9FfN7Tn0PJKg35Xg0EPY6rJbtE22lWmtqF3llGRZ1xpYJnGU0clZ0AR99kekhBr1fwviiKZD8Fgkhe8_BHW-Z-Rq_yTa0VP0qQ71Mq2GG1JkEmltqgTHLSXt1uD7h470zvFVH0MY7BD0kYZnbgF-V3OxLeDJJUAuxHBVNPuS1cRF8rRs6chzIc8aZyEKaNKy6bQZLu9WC5eaSUI563R6ig2lxAknCueW0kwzA_kVRlRawM1BLkBRZBj22c_D-EdSzI3M35QFYSHcwG2TGNDwBySgwhnOiGUP-tT9C614smrNYgAi9XUSXLLbMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGHAwpLAzyK2IIQn--nXU3vhK3hdJv9-AnERn8RDnGU75092kjqixQ9CsODeQ9PUBtEAieeeCAyuv3y9OzBOJqbfGAnfgxOm8ioFBf5gZgR_c5H0OeSQna1Y8cx6n_SFcXV_TZdCYiAbISNe5dKn8pg9aJdmvJE2431J3I9wQVfaZLcLAjrUrrrvB6PNUd5a9YPUJ-XQ7BeCtUUusZIm8SEevhNyh-zaC13iXXwsfJVpyR9tVhOjgC4V-DBCtOE8WUJ-Bztx3ptq6p5DNs4sHhljxCo9QdSM5NyAPakRjlqx3EvjjNRmYqMpGMzbx7z_OsIIE-EHE-6LATXcmR3tyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N43kgUozSSkq1OQmmtS3Tqf8liDo3Aop-Pr6SvND1MKZE3NtjVFNkIjFdmnmMwg5MVb9mISNOhMG0AIPz63otPnWtcetwq1rm5gw904LvPB5xLurb7k5Xa4tuy6fvyu0YCiK48xeb40ItUgEuPnCNXnyKxvDu4oa4rFPnQTX3QSCHvAEXVF3M1iP33YWTQbc4gV27HvuHzGTJo-JuiYdZDx9Yl5vJAJ53_oq21vlFZyk2I6N-01DyTZOm-BeMV39gCy13uO2BUrFriwwRLWVhzgGr-6sZJ57NMubna7eF-0KtLjTfh26VnAToHglD-IIVYNEidVdJP8cX5CHTBQvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZhmxmxUnVEfom16qGSWIxCiE1QkNdrHVWhZyGM1wh2aUk9N68UhoqgA-yhPuQqrc6FWdsG6Ek7zZoNDyNCaeqHXtZdkPvUUdEnLQpeHTsx1UkBK39u9jRpkGJVqkwoG7vDEWAQHDbQDBlqIAK1rpU7mJuvwiH5uTwTLbyh1h6ZH2jiHU46qzlAokjb1NHHGKJqle9Op_Y2HLC87BYMWw18RfXTotTPtvyIvNzCQpaI5H6TrKxU0E3Q7t0z-RZJDw33ewexLkf1bwOIOK9ORwVOC93dAQrH_U0F84ubyIcVQK_yftss1RgX15i9Yv1y_acJ3xYfOILiJiMZ-25_27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALOV6gKwqhM-uEES_uA33OnMdftVFctOtB1HwXgkJHdzIzR4YgekP3S7XiaWVDDv9-VYetn5vrTaGdarlk8yRbAB5cm-an1yFewKydxzhB4w9rrAIQbvN5wfbtMcbQprm10uiUSluC23uQ7KLNwQGWjrSyHMpsdEUj1N-Cul1OjEEdEdQPXBi1XaFsR3_PHagNkSl4Z7RIq8UgmVBmjTPhlNBeqNjYLxaHAzl8U3lm--gDFBFzfy47P41Jq_bHW43GX6n9x-4omFWoeHEDVMf_mBo4Uj7YKbNu4i8a4ANatS85tJi1C-XTEuafs33rczrXu-1YLEvte0eb7v-JklkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIVsWKwgeffeKB7lxb0af1PEqQiV1gu-kmQ7a45hn0i5Hu2Q-So14mR2RC6ZUqAWEEISAMOuVgBmbmQSeVBmm83xMGSdxxOEMrF9ebrmrr_Qg1wcIoZ5HD4IDYDEmM8fQ8ZgfundEOjBZT9sK-0vwi6XdMY22XT7YN5QlswIndzzhC8meMYFMd7_KK2McU6rlG1z6od-NdT1H2kwbJ4L4RutvzQIKlyKJK8iZRimiWVQfDI7cihoqHOCGlulgAwpOreNDqLt8JSht3j5Jz5VmOYB-Rc2H24mpx7GzjGYLCVPCQEg64evbydBQIbQ-o6Lh7A-S6VObpAZqKd0y-07DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
