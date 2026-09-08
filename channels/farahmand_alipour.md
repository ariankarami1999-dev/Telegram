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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=FaRyVhtvrmWg-kGoQBE98YF21PC9ZbMbRxixQtdbMsZqhc7rY-y5Oer2AN11oYbegsWDH5OjDx8YlgyxDk72MahC8I8Ba6F0PucRgi5TpjGfbOlujbhJ5ECMq_Oq_ftjagiJ2V78ThxqJ53dAJSXzGUlR4Vi4O1Osdp8IMC2IfaOVs1NPVkM9wFN39ZAOpMDNVzxseTemd42-EZhaKG6da-QLtWJRsjbyJyT9Ve9kf7AoQCjmAuB2Sq_aQpW2kQsubT07uqB6boEBBYwRh6CRyaM4-AEiqOdWt9fdkb4rT8Csx20s_GfC9dy_Wmyqz1bJoO4TaZhQMC5z5L_zs7FczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=FaRyVhtvrmWg-kGoQBE98YF21PC9ZbMbRxixQtdbMsZqhc7rY-y5Oer2AN11oYbegsWDH5OjDx8YlgyxDk72MahC8I8Ba6F0PucRgi5TpjGfbOlujbhJ5ECMq_Oq_ftjagiJ2V78ThxqJ53dAJSXzGUlR4Vi4O1Osdp8IMC2IfaOVs1NPVkM9wFN39ZAOpMDNVzxseTemd42-EZhaKG6da-QLtWJRsjbyJyT9Ve9kf7AoQCjmAuB2Sq_aQpW2kQsubT07uqB6boEBBYwRh6CRyaM4-AEiqOdWt9fdkb4rT8Csx20s_GfC9dy_Wmyqz1bJoO4TaZhQMC5z5L_zs7FczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1SdukNYvvy9mfr1Agx1dIPBj7R-ysewpmPD9QNZP27PqkU-9oFvEnvLR7Me4VdkCtQVIcjM5Ji58i23rILMtEOpYtM87TS5hDKPM4CX0mmo57WC2uMvQubaSVy8K3mTVoveun0qZ9Ll0nBy4siOQ66kIGYoEDgb6AD00nst0XyitKJzcme3H7QJaLZGkRpPybYsCW953Kea607TKcnHcOpyOQALGXw35WlElvwwLBbgghISuYkYBs8M3jtPTnDw1d8YQYVjOQ5tt7hbQnJMrMVKjbT0E9tZSBOnNQBTkn90pkpw7y7wDMtR58tQFgC8E02CigC7xdOsKPYydNVixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVZfXl8lZ58EPhTA_1ve4hs6oGwcTaB3e3lcTsxkh5udB_RDIQqhqdgAoFIiODHvTJ0SPufPUby1guGEV6BjWlJgGemSkscePpmNwzAvyarroXsmwxNVgR0Ou_mK6hTGkvCYrAXZvnqnYBmSgk_VLpwnd8oK_dWiGn-uQmT7raYbD6Mn-jPsV9GbEt8bAcmzDGjJGoFFsXlTSQQorvAfciIa3UwfTZ-H7KwekfT7AWUnSCd9POl60bAEgsi9BgfOG5zC3LVeYlAM4yEUKSkrzkYykW487XMMwOpBbVKYK_4hcgBuGZCC-NAbDbwtyFs8FJPbb9yA8Q-4l_lDJ7dr4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ZH63c52aGuVDOx5x-Iz6CYAkiqwTYdGeadFizYF_S0QAA1JuHhqjjWFbIUa-oq5r85cyes58JTSFODHMv--zOTySeCn-Fum98Ncuz8ch18FUeKUCyza9qNiEKpm8BC8d0l5pmZxUXOJMfMZZLRR57aSQR4ftqPNbwFSwlMplBPVDNZ-FE_AQhadK7ZuwixMKelBaNohGa821wuRTb-u881WGiGzeCOEqieJMuz5Bu3M9hLNol_DmaUHX0VP4LzEQzHpnoi0DHB6kGbHF9R1CsA8yqMTKi4mjqoQjJ0WLBRR7KNGPpZ4WyGmbJytICpU69jQG8DY6ZTONpWp1TZhizA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ZH63c52aGuVDOx5x-Iz6CYAkiqwTYdGeadFizYF_S0QAA1JuHhqjjWFbIUa-oq5r85cyes58JTSFODHMv--zOTySeCn-Fum98Ncuz8ch18FUeKUCyza9qNiEKpm8BC8d0l5pmZxUXOJMfMZZLRR57aSQR4ftqPNbwFSwlMplBPVDNZ-FE_AQhadK7ZuwixMKelBaNohGa821wuRTb-u881WGiGzeCOEqieJMuz5Bu3M9hLNol_DmaUHX0VP4LzEQzHpnoi0DHB6kGbHF9R1CsA8yqMTKi4mjqoQjJ0WLBRR7KNGPpZ4WyGmbJytICpU69jQG8DY6ZTONpWp1TZhizA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq-qDV0w8shy1jeStwRMjipA5gfNDIRI8XMxAOz-q_idAjTng132C-4UArq6B7zAQMLHXGTgBenZF1QKIOy00Em9qsZWRF-kJl94uzcgTKBNSEbPpICnVquRW6Kx8eUc7l7NLMm28gyRakV0mNtsicbYFWl8Gj_OmObqtpEQk5K3_c3scZAvagPdmMIOeKNwkywVNGeiDA42SLRODO9VwOBxJ6rIJXcQtYhFO0JLrXKaEAJWXI5b-9E5I0-VjLFLdN7_HlZCd4ykb7HjudtQ5sl88ltn5ICBQavnQSQntCohyaQVP35vRsxFwfO5Hln5dzgS1juagzV11fzNJYkwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=gNTkZbKYkVqgHYWsoXJAM34SWmE2aGOuwiH3kRdyN2xh-LdDmSxPZlO0REY69_dhz49xjY7EoQ7GjPDSn6eathT5Fa3OT3c6Y0cnMqSezRc0KwaUVfMpyi_3GqUmuhP3FV9B-cyzOXoYzBabJo7yCwUi8Rs-B764nC0_fS_Q9Nwo0BBW-Jai4P3dXAP0_6Kp0DCIEMVI77u1q-rzaIdQWsweSdFuZv7ElK8K5RiFW9R90QE8_N7pvAYeg0L9axrytLZ-DHAhNJcBsqAVkJZfDjwspNHpclSqJmlT_EyIqAMzrj-PBRlgQKkBFtbjsyUZ5WI7_zF2N0eGQTO9QAYTkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=gNTkZbKYkVqgHYWsoXJAM34SWmE2aGOuwiH3kRdyN2xh-LdDmSxPZlO0REY69_dhz49xjY7EoQ7GjPDSn6eathT5Fa3OT3c6Y0cnMqSezRc0KwaUVfMpyi_3GqUmuhP3FV9B-cyzOXoYzBabJo7yCwUi8Rs-B764nC0_fS_Q9Nwo0BBW-Jai4P3dXAP0_6Kp0DCIEMVI77u1q-rzaIdQWsweSdFuZv7ElK8K5RiFW9R90QE8_N7pvAYeg0L9axrytLZ-DHAhNJcBsqAVkJZfDjwspNHpclSqJmlT_EyIqAMzrj-PBRlgQKkBFtbjsyUZ5WI7_zF2N0eGQTO9QAYTkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=R_3MmvPYf7udN-eNytxRPadV6x0uiyQpgCRwRvhrkVnv16IEBX06bNMluZ9xUjUM8u9H5PozqFXu1_reQ_ZqCv47BBX3VYA66N1ffdlvhcytf9cThZsVUtkVZ6ggVSsuovpU7suiwP5wBMOte9JjSfTbE5wpcabhs_bhZY0DvYpIX-F95eWzahlwHxN2gIagKw4OSb6QdHcF1Rp9lI6E4HIMd2josVE4JkwTmAuYXbIvA76X-C8u9Vd5XLzROOPNsRVpqXLNPTE5USKsLhysZCow43UCA8IKa9pRipyNylyCb2n2eR5nrG1dQ3qkTea-I6l_FYF4c5QfKJnWCriY2A8-_OimKdjUjiAfhP-jKoRbSlDA7OiaNr-nPme6wngGcNr8cTBM6pUGYX5DY6RGd3pFAYxATcquN0ZLYRihCTTb2ZefaQjrw6Uq0tczyx35CQUMg5rBCRdIibEiKgzFb9hR9OQvnMDe8DgmbY2-WeBbBkHBpnsRYod4WeVTz0mxaJJHX4bm8SqUNwImCw_yOUZ-0xPx3Qbe_0aaSlUiwHX3YpTMgVGAIh8KJqiADugDpX8jijdwfjPTOJum7UUL1IwBg3wjvnqfIrqJzN2TbYHMXcvIuRKx6GUVL0T2IGya_GZ-bapQq7yejVsMDIipX_KfbKMKtC22aMUMQG8TaqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=R_3MmvPYf7udN-eNytxRPadV6x0uiyQpgCRwRvhrkVnv16IEBX06bNMluZ9xUjUM8u9H5PozqFXu1_reQ_ZqCv47BBX3VYA66N1ffdlvhcytf9cThZsVUtkVZ6ggVSsuovpU7suiwP5wBMOte9JjSfTbE5wpcabhs_bhZY0DvYpIX-F95eWzahlwHxN2gIagKw4OSb6QdHcF1Rp9lI6E4HIMd2josVE4JkwTmAuYXbIvA76X-C8u9Vd5XLzROOPNsRVpqXLNPTE5USKsLhysZCow43UCA8IKa9pRipyNylyCb2n2eR5nrG1dQ3qkTea-I6l_FYF4c5QfKJnWCriY2A8-_OimKdjUjiAfhP-jKoRbSlDA7OiaNr-nPme6wngGcNr8cTBM6pUGYX5DY6RGd3pFAYxATcquN0ZLYRihCTTb2ZefaQjrw6Uq0tczyx35CQUMg5rBCRdIibEiKgzFb9hR9OQvnMDe8DgmbY2-WeBbBkHBpnsRYod4WeVTz0mxaJJHX4bm8SqUNwImCw_yOUZ-0xPx3Qbe_0aaSlUiwHX3YpTMgVGAIh8KJqiADugDpX8jijdwfjPTOJum7UUL1IwBg3wjvnqfIrqJzN2TbYHMXcvIuRKx6GUVL0T2IGya_GZ-bapQq7yejVsMDIipX_KfbKMKtC22aMUMQG8TaqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LmsemA7ZMD_x64hqUaDPNjmMtdIfwtYZCITBG2_v0Tdef1AFvI8q_5Rzinox6VCyAekKCfN6jo-5fpYHIuJCia7Uv8vLwTud4VVDNJl9bqDViVu61r7vHAVvyFQ5zxvaNty2APLE2IoKucuDwjMrlm-jqXViJNwrJyo0pUmDi_syPGUeBmS1RiEMR1S0_keUiBrZF0Sef5bSwBA9mlf-yhqVsA2raaH0AIs1wfZFY-IE9vD-gmwY5rQEZNN-CSyr0t4COAQQMRQ6P5nMcDbqovy2byUy2L7SZUkwYVGVvncWSnGattHYtcPsXezR3VlLw6O6Bq1GmZjhrECRCgCvG3Z5NiEXzoyZxFhtgFssNl3g-b0dnXj6jWFCiyUs89c3qTHjIeo0rmhdTdlqutFumnc5WhF2Ku4awS_cTiZOgqwll5Uljb2VFcFZr5oVlBSLO1bIAKUa9ImxpwPd4vJF1CsKWGzvaVRmDv4F6YN5Y2dNDWXHfFCeOYzIwnbo3e_YK-rDVFlA17KXk1mjscDjbeSEKVGfy99qvUFB0Ns1-if_fW1twSeNW2a4eA4rYsc7vt8wseVv9GhvWlg0HYtD_qockCbTZpkLV94pRquaXV3QphnlLaf3dt5yYGibp_ozXl8H-I3z8FT3JhHbjDIa562zdadSL77gzCVjR6Tg5aM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LmsemA7ZMD_x64hqUaDPNjmMtdIfwtYZCITBG2_v0Tdef1AFvI8q_5Rzinox6VCyAekKCfN6jo-5fpYHIuJCia7Uv8vLwTud4VVDNJl9bqDViVu61r7vHAVvyFQ5zxvaNty2APLE2IoKucuDwjMrlm-jqXViJNwrJyo0pUmDi_syPGUeBmS1RiEMR1S0_keUiBrZF0Sef5bSwBA9mlf-yhqVsA2raaH0AIs1wfZFY-IE9vD-gmwY5rQEZNN-CSyr0t4COAQQMRQ6P5nMcDbqovy2byUy2L7SZUkwYVGVvncWSnGattHYtcPsXezR3VlLw6O6Bq1GmZjhrECRCgCvG3Z5NiEXzoyZxFhtgFssNl3g-b0dnXj6jWFCiyUs89c3qTHjIeo0rmhdTdlqutFumnc5WhF2Ku4awS_cTiZOgqwll5Uljb2VFcFZr5oVlBSLO1bIAKUa9ImxpwPd4vJF1CsKWGzvaVRmDv4F6YN5Y2dNDWXHfFCeOYzIwnbo3e_YK-rDVFlA17KXk1mjscDjbeSEKVGfy99qvUFB0Ns1-if_fW1twSeNW2a4eA4rYsc7vt8wseVv9GhvWlg0HYtD_qockCbTZpkLV94pRquaXV3QphnlLaf3dt5yYGibp_ozXl8H-I3z8FT3JhHbjDIa562zdadSL77gzCVjR6Tg5aM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=QXYvXi9gOs08KWzpY5hifYmkHmdX19VGvvo8MM9Bz85GGG1MsNcC5dgTT-rtt8k-ye34b2TZYb-U8OvKUUD82qd2s_dLTTbn4Zas1paQrJVxxQGc3cpa_d3a2w9yatyWjOnLvo0W2amQ6VV4uqc2KyHNLYpSmztFxfWJAWKfSqXleUahPvawQ2lWtSDBwielwW3xnR8QoyeGHM4xNaQ8_eA59fyIpSeQrMynRV22mX6kx2NFr5P4pXn3muvpVigRV8ySYK9rwgXx8L7s84oA_RSUN1mvwDitwCJJc5vDqT0CG78JyKykdXel9PwUBnXnei4HslmSqvQaLpd5ZRiSwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=QXYvXi9gOs08KWzpY5hifYmkHmdX19VGvvo8MM9Bz85GGG1MsNcC5dgTT-rtt8k-ye34b2TZYb-U8OvKUUD82qd2s_dLTTbn4Zas1paQrJVxxQGc3cpa_d3a2w9yatyWjOnLvo0W2amQ6VV4uqc2KyHNLYpSmztFxfWJAWKfSqXleUahPvawQ2lWtSDBwielwW3xnR8QoyeGHM4xNaQ8_eA59fyIpSeQrMynRV22mX6kx2NFr5P4pXn3muvpVigRV8ySYK9rwgXx8L7s84oA_RSUN1mvwDitwCJJc5vDqT0CG78JyKykdXel9PwUBnXnei4HslmSqvQaLpd5ZRiSwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=pbEyI7BINh29hF2XCYJXFBE8XIg5DUxotGsWliuIW2lwi6JHiFrrVoUC-F8B7KA1tnJOUHVnN7G2VPq9A299iPWWSJDP2ReB6gyMbCx4p-YmXI8ybYEtyHo97eHtz_TDlvogJMkIWUafA9C7XQ4wfS_epF8rMDH6gj-nHyo1iJ9_n1cBGJYRST8KHEvyXufgFR2aCNMJ2drIcNhVGmhvukccHSkpT3F8Vrj3saqPChZ7AMExkTLGytUQwDeJWHeTnn7uLr9Hptvq1Z5Xc6PiEeBg1zIY-YE8RxIIDf0KINUjEjP9BcbZqdLXzcQronCU9CXkrDf1aYdeTlHpzmIQfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=pbEyI7BINh29hF2XCYJXFBE8XIg5DUxotGsWliuIW2lwi6JHiFrrVoUC-F8B7KA1tnJOUHVnN7G2VPq9A299iPWWSJDP2ReB6gyMbCx4p-YmXI8ybYEtyHo97eHtz_TDlvogJMkIWUafA9C7XQ4wfS_epF8rMDH6gj-nHyo1iJ9_n1cBGJYRST8KHEvyXufgFR2aCNMJ2drIcNhVGmhvukccHSkpT3F8Vrj3saqPChZ7AMExkTLGytUQwDeJWHeTnn7uLr9Hptvq1Z5Xc6PiEeBg1zIY-YE8RxIIDf0KINUjEjP9BcbZqdLXzcQronCU9CXkrDf1aYdeTlHpzmIQfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rchrkimLh9enYKCq6fofQW3KgH6Y9CvKiUV8zLaWj_Iu70sfMhZ99XTwB84R6L7NKzK273K83UHh39MoEvOCEWFVsX-z1TmC3t-GrsIzTb4zEZGShPgUTG1pj4g2CamOsz5xzUdowkZ68Hv7l4sR0ncS9DKMwdZ577YFb0M-ACt6IAw_P1lRNxfDyv4AgVuFjNtJt5LO-VmBCw6Sb2O2guFOzSmTFUc5MFhQr8-2NCoNpOWMlIk96eP0eTZ6u2fqUzmCmx5ESiNsq5EzFCPjJS176dZQVPGHjW5vQSXdaZg6iA08_jLGxUcoB44tdPRl2oGtF1moErsT5vtYGHaQ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY408dB_EXlrv_ricepO0ASJj7ETqHCVHDReQKm_oEaH3v5iuW_zOnmskty4guJ71wNG47tkqUCEz51AuYKbksE5I-oo5t85WyELAInrapelwumoF1DWBkv48GXCiVMqvymQOPgVkYyWu6ZuLn_QggJOJzpzm-k4z-0_UteTMw31sKXe1IPx907VUpokrNdhQCzMtZboCj-C0SPaXy9mUEDMZ5zQyoueT8jM-5U93RogQWDJX7J6MuHrU8LmUqLDgrwUVZyjmcwbvVzvykJtbjdiibnbME2VY6zAVmdBywRuPeJx8L9a4EWktAff8I0MHXHQ9-UhtkULZFJQHazTLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6zxwjqbZivrq7R-Ii9QAVhOoyEyhMMQrW8jYSE_K3HSJlQiGDyzQ6VVXmavPRX3Mczgn49gFqCnZfwhE6yl4BgDX6RfjylMxkEG512ZDnsDDM-7u6-766DOp-7A6NTxBtCvt9aU-TnMR5J9KzUy-9GhQRByfsNYHzIsMe_maqOlGqYZ1Ggrnui85wRWnTJQ-VOBs16CSTa9FkAl6zDnNgv0BONWTjTZdSRNl38nhBCPz40fHizJGBtFeD8Tcbaa50xJTDIACQC4MZ4Sg5IZRiqsihsCBL480_p-yVS1GtRHTuxjW0cJuRVOC5vm7ukQdlomnlLMOArTx1PDVAwp9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRPDSAL4zvNoxUpXjZk5GVAcoV1_WpgwWbtq9U_Bl8ooZ5rJRt9tUE21eKURaVBRBMNt4rMj39Op0IONoVwdzOhgQL-xmYKr6-n0tXEJUBlwNai4XN-wSqDqIjSFE3--hsmticQv9fkhFiyMc-RxXIabajC9wdOYng51vF338iq6kOtA5UNua3IZ9mfFAWRI9p6gvIecWDswPqCvc94JzIZSmpSeH3_muNIx52qgVkQwSQQmesyK_sFCmLkqZKHYZV3QxmaWOKTnZrHaKnY-YWBt3LEoOoBXZI-WRIl31Cd68R856m7KCYnrshhIinxacMATCzaLRzhVkhLI9lFCPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLCQ-ZbIQyIo0a8JJN2-ZnF4e8eN7UkQ82e-Eh73swY7hzvicCcwGsFYNSWTNbNzuk8WhNMhPV2cr3joWwlUeHMSTnp_RZQodGpA8OTID4R0rJ40oN_KRTuWlTmrdS7qoZEnXiqQoOsuDNxUvYosLzEnUQYlY_3rcOWNzJqd3cg27qvWsRY1xpUWryLsh_jib2ebm7uOZ5UsHpLf7IDB1jxsg73lTtwiKZfPhT_4OfGfnUnoc-TaLv-LlvQ6m_q2I_025fSXa7xzv3QJqhwuc2ynKjeV19b6su4T0UOyzUyEDiEtf5icKhmJPKG3JhTColKOSH2TT1HDGCsaEkx_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJL_AEyLp8ZHKpgNrOzxBNJs9n7yzJ5stKg18pOhChkxTJxNzELXszb80RI6iRYKDp6bFztJQG4dDPRI860xot-2Go3inTqjv2vhorZJDxbHow0UpvIgkv5-R9CwOnFuysuT46RkHRYjiFZI5_e_zzTLoYIs4GqbpJebqUpHG-Jr4yqCuM9UMXAvg7n8bUiom7tECdWUJMfk8Zeet5mp7GWSBMJtHxUXQNMrsSkAwL_ql9vVamDFlV7gNNziZLsKYhaUwntn9sLIO7yYMTw9PNZvgd3DSEc0deuH-TxIkInigsN82ClXzfG-8DQ1oQo4uO11HWUz9ZaV9mM1ij1mWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZBX4cmhFQH5VmMb5dcoQ8ETaiZsh05633Mq_ortCrD0jEK13N6g3ImmKaLxq4zwXeb4RTiXSLyLmuLLTPzdi2rL7N7L60KLEwz4OELgUvxZVpH-KXMDrO5YNun7GErf3gKh1HeVIvJcWyBZfMqEup7_O3yx00vM9qaB0YKIivsRukeoFOt9Ghef78JaL6kx5ZZNaTyyUrqbjStErStyVDdC38YhWVceHkuZ-QBZx0K9mESZ_KFJ7LzM-qHesRC5ak5GYdJ16elVVxcY0VekWsIsdxH6ejlCPUjxMgO-doum5GF6wLaao8XU8JV0ahSGV0fYVWByB6FmbEoyZMcKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmVaCUVkeKMABL_SZuD2rnVrOBUcYXHkjE9P47olDc2QowtRcKOsNT3S1zaKfe-CJSRLCN2vCGGPvW2qvZ6L2VMc-_jUzgvtRtoGdM3ANNULoOZ-58Ol8cSEAw6zURHhAK66cDCRsTotMgGjag7xdBN0y2uNEcSASnYGlBgT4dr1BRm8Ul28gVqSzsnV457-DNG5IQVD5e3iVgYTgA0yJSNjkxcIyUmLAvrnzipPpxGJZafJllRcHL7BGcVyfDC29S8fH1e_pV9D6bEfoZKRYo0BATnbg76vAt4gPMuGwuQqxT4MdE8wbabsA97LoBjHWkCxWHdjVIreULIWnCQ0JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqmHtIcmTnZ6i9dsLleIClftBg__LjtbiO8yoYCQkUzOZbrqZUE9qrjEQS7Z7pGv-Y5vUxMeYvqr_f3NIjhePEW_PAoNTbvtnzYwfi-vbTDHE9emi5GvwDNIsmui5ZvFs6FDbMRlRjsBDpeuIW1tty2yFITeVwgZicUpBtN6oeAD-XZAKPFg-vTqoFD550U16TR2raDQs3zMrt2e7LTQgD49YxK_Avqh1Rxw1UTrTlaxJcaMJONChZ_59CVwFMnMTg003NvtG3PquhGKYzWcQ1OFyKJ6muR4ZGM6g6z_xE8-ZzFiPSJCbTZ-iXb0s757-_t-clW-0JT42_2hU1OI7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5XBTf-UrCofxMrLJ1N1Zt1gVdf9e8FXUjSEwL8L3WAVPRjFYjxRE8wBIo5ceEgROAJjxGWksj4Eq_3HM9iZrg3Sl3kYIYAOpkxX1eGbA7q9lMFPsweOx7Yd82pKJCpqMXO2ev_gnyZeGFYHjRIDfIm9zS33TxEexbLFklLQ4Iezbmtw3cqqo-vKJKPfn60UfJh9ha-0oAWqhtHq7YG-k1-nyHGDtUKg4iQ6agTWMwwgdW0ZSt3llaE5rHiVAMhs3B_SHKg22mR085u5EGxQc_QEcEk9hH4xczAve3v7NXcj8i0z2IoaZYvVTsiMFwQ_jcSBV1eBb5yyMwP-hyUglQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Lv7h3sp_pn5ld0azx7GtQvx-RHyY3rkcA8mX47omE1hz6QflKkxFnGacsq4XZUetxizli4n2BFqmwvoYmROOv5denhRywcA89fTCqvSbF-txyPPnhEbTb5Slw2eBKS-0L5NdKZpDJHbvBL3m7SuoSIZV-Fp2qFoT3Yypdgw0zZM8vqNxjDe87rk9EXlHtH_ZN08avuiiK2z8z7-Z1sMfTaE8qFOht4HE1z4Rcz2L7gqGlTisHNf7lnmK6C728iDhBYWgjcOBD-E1jRPmqVrJG6VdmX8AS8-s6o5IEq4ebzsjSA2KB3KdMmI7kP9WdVuSPzj9yEHEVAv9LGCBjZ8sbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Lv7h3sp_pn5ld0azx7GtQvx-RHyY3rkcA8mX47omE1hz6QflKkxFnGacsq4XZUetxizli4n2BFqmwvoYmROOv5denhRywcA89fTCqvSbF-txyPPnhEbTb5Slw2eBKS-0L5NdKZpDJHbvBL3m7SuoSIZV-Fp2qFoT3Yypdgw0zZM8vqNxjDe87rk9EXlHtH_ZN08avuiiK2z8z7-Z1sMfTaE8qFOht4HE1z4Rcz2L7gqGlTisHNf7lnmK6C728iDhBYWgjcOBD-E1jRPmqVrJG6VdmX8AS8-s6o5IEq4ebzsjSA2KB3KdMmI7kP9WdVuSPzj9yEHEVAv9LGCBjZ8sbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9IsGywxVo8o06hU-ZFHSlK-kGOulHCxeCWQW9oF0hFMBH3FIXXSjuSLiWDUH1VuNX-qn20n63GeAdQglYgGt9hWncFS2J9xC5Gda9YOW-tnu9GFaGbV-bIVDcqYUwn4LeVmrJEXWSNVvETjdcRwBOJnPSpzA5d4lSxmv5TQ9BAqZljK8dlommgj5idsKP5_jEjcWh_LFfYmojpS5qepasOnpPDqDrmX634twzb3R2r6wM8kJs9TFuHfkeJjjEAL7z7nczic_PMIxUqXQiw0HyZOIQCzWl9i-LOmlkLBzopuQByzSnW8WE58HrnlTvtkb9R4MdSh0-btR6Bs6LgFHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeQewqbd9u3opgBRMgFBt7YerUSpKf6RgNZ-49LK2Hwdm1l-mMti0wNIbSCSzNl6XHOOmbdG7ZQobEdqmmJvjBcivTF5c2dtR3Mb1hClh3-jzN5psAnWx1Akqvjs53u1g5YdRwEdmKvwShqz4-75B-dvx65tEzllp_4rLihrPvchYtoNq0gspXcELbrOVt1wIAaIBr4_8w-xCGqocJkXhftTnTK3nc1SMPB0R-ZKRlo4idxXstT_pMb0aTyVTyJ6jx4mUcByxZgZleaM8U0TKviYBbO0mWvtururkfQ2cGaSZ8IdEj1UBqejyrTbF6eLNo7Mocw4W4_k_tpdK3mKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=iy0G9xF3G9-zuUh-Hqc4uTQTMiMB5BkYQRZEbcd8vYNj9vskUygIJcwFPdU1diN_cM5yEmPeLi52_iLwqcQPU2QhOMNkHBeYERJ5r7dCf5ic3eghRtWTL9XF2LATRZUjeikT2tQaQtMuWMOxloHpQVRV80Jre6zGsEx3-wcvE_nbebeuVP1J5xSC1-s_t1xFx01svw3MVFiqWQYSUr8F1gns70027UQMS1b2iGtq4ejzEsRWLYSjuNter3ghV02tuMlmPfGceU15ZJcDAVJ5TUz_uHoK2JswBislXUMvuDXXkprt3wzAIKHUpqnUheRBO88Fe3VKLapP-C7YXqeYvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=iy0G9xF3G9-zuUh-Hqc4uTQTMiMB5BkYQRZEbcd8vYNj9vskUygIJcwFPdU1diN_cM5yEmPeLi52_iLwqcQPU2QhOMNkHBeYERJ5r7dCf5ic3eghRtWTL9XF2LATRZUjeikT2tQaQtMuWMOxloHpQVRV80Jre6zGsEx3-wcvE_nbebeuVP1J5xSC1-s_t1xFx01svw3MVFiqWQYSUr8F1gns70027UQMS1b2iGtq4ejzEsRWLYSjuNter3ghV02tuMlmPfGceU15ZJcDAVJ5TUz_uHoK2JswBislXUMvuDXXkprt3wzAIKHUpqnUheRBO88Fe3VKLapP-C7YXqeYvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=hV8lXZoPocU9T5LSrlFhinHqZRE_VSk7ZN6J05G6dJdBa88AQ2aM49r4bhk7YGeF5oc0zHKjwVw0WTmDIM1kWXSxWS6VIHcQUSL37sagRrzjhG8OgoOaceuDFYUp0svoGt4oBVOaUaxnFu1mmNl2ueDILOR1PPVh992JO4LprjNaf3aZNUuNTr2N2k_ievg1F5UkkzuNbGbvDWi_mbwucaiPswM8OKB-jc5VEuWPvibT5zByNsB6mNm8jydLyruOmCoQWjxB8-9JccFeTX6Fx3phnEu-Tv_lHff8YA_KsnkduxhnFAAFo_5oRl1LnkjHYdrA-h9WUNfFBGzAD6dWLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=hV8lXZoPocU9T5LSrlFhinHqZRE_VSk7ZN6J05G6dJdBa88AQ2aM49r4bhk7YGeF5oc0zHKjwVw0WTmDIM1kWXSxWS6VIHcQUSL37sagRrzjhG8OgoOaceuDFYUp0svoGt4oBVOaUaxnFu1mmNl2ueDILOR1PPVh992JO4LprjNaf3aZNUuNTr2N2k_ievg1F5UkkzuNbGbvDWi_mbwucaiPswM8OKB-jc5VEuWPvibT5zByNsB6mNm8jydLyruOmCoQWjxB8-9JccFeTX6Fx3phnEu-Tv_lHff8YA_KsnkduxhnFAAFo_5oRl1LnkjHYdrA-h9WUNfFBGzAD6dWLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOj-wAfaR6BbN1qYE8AJR0qDIdglJ_blXB-O6KFKMQ40WH9x3uhyD79oh5EpkBBL9f2WuNl1pq5iEEgk2gnVPkL8SJVqPcEgYzgBBbqrHOe7hTz-KvCCQZIif95nVW_Jn5dWq5HI1uWdLNxONXtvIGIN_ndSkzJof-jJmdYcb4FLzyfI-jPyDZOtZ3_j1Stp-903MQ9RqLmd4RtMI706BbSA38mGmyNaff9X-8UooR0qHxZfsLCLvds0B_Fj-BbrHafQox2myoEDOyVcNSUX8sv5sQPD4q2kAcotEO-w6abtzbJvp4Nyn9OL94_ZEf3qNN9RioV-gMryTW9dlet5nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYI_VcqKSbqwUv-94o8AoU8cN767OUo0GUIm0Oo-xYhVGcxvCgPe56G1n8fBtfu2_6RhrjV3MXsWo6i3brigswhasfhQk2qNxe5uN59-3lMGWXUQjhpEjn-a76u4qSIbzRBfL7rmTix7u-MkkVqVjEiy8uiBV7nbpsjIcSbuuQ2Z2apXcpCD8hhsgoIA7tEgxrjYpeqixdXy-yYEmTtqzRq1xadjo6Qac-WTB2LD_l0alLwzc8Y0dxjsJe8RG-og9AtwIg2VjUPAQVwD4pOz-0kXeoWMICxoGwrn6ZH7ebPxgPYn7BRJ8S0s5htrvGiERfTEwLJr68osPbphBhyApg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed7tnBNYYTvrDUr3FkIbDbWMTHIYC46B2iC7VuY6aiNQAb11wU5Cmjzmbpbls5p9lT0VokPylbKMufGoZbwTKq7wfYSuGAlNKQmEtd0Z6GQB0aR_muJrt_79gKqr-_ajK4Q7K2ru1v7-9gUgUH4eF_ENc3Evh5GIQDTLUbDliLDsZvOL62QqffCUJSB3ReRKhdiR6SkAQbSG4WGgajQAZ-zmS_y5AOPZvI5l5wHsdmRRBFFae6JVeTwROu74P_IKGJoLpBCrqz_VCXfiBfQK4Y6DslF5bM7FJ-7YkOiHEGaDKYyJaYHaXbXE4MYo-hYrR8m41ztcPVz5ukhB1DQzlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUkSxkyYPLbWXRXjyC974tYqGMd3kslrrhMsKQvTdVCal4ewFKQdxzfWdS1-8UmomJuXKXpo5GTTH50uqf9BfZxTVkRHxCRuh9i_EhNotkcjDcVTqxn-ijdrItzZPJivO8qQ4A65FhjQDfL-L8tJ4FbgPhG1Do3PjnGowwnk4r5kbb4EY5sQC9UBtlhpvKEEUzRfcELGTn2X6iFT3wS-v3pVYuSz3aG5ucwQguPsY5k2K5-shYM8BYUtKj8p4PCuZHhwbPfRVIHPRQuuIpTWCzZp0Z0Z5L3iKyTgEFHt7XoX8emdChhlT3sy2n1WoLoL_lk4UPdJoW_cOacilR2MZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIIKsW8Excza1dL3-30R7OOvuXR04OiOrD-p9OqoULVbkdtdQhmKcvhKAw2DXywPZJg3nTH0tUm8AE-8H_hHd9JLti_JA7FsNJ2GgkEcASBtPZDmPNOuE2c5TzvV4dLKHOBe5GIZm8-MKy2BkYvPEjRTqQtRCCBsALg9M4VcOgZ2-ZluMkuxTMbHS17f5R7BZDsJMHmWx15zpQBUeP2zydWvOBbrFhRSIvJYxFHiDc8L19uq-k_0xv3Q8aNyrU_GHcAcFl_LodW4jMXVgMIwTcAVTX_osA9LIKAsZmTbOxmTgYzDbXf0BZtS5bpxmIMgPJ0zoKNBdqUWgTfaryUq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJMbt-g38aqT2rxvVS_KZ87XXhs-PFDfH-bDLEl4S3xs-JkP54QnM2B6-9kKQJ_GsHHPZ3M7BSk2SMq_dqsl_3D_rlI_47U5wbXGuqITskcpIyL0KmOb8XBkIEpHAouqSX0fI39kdJLlVnSh29R_Bt-uViiBNgqIsW-BRjdPbgwTlxfDsCRjCm2VFXJzq-Cjq51AVj6FQT95Iq5VYwhMtFFBzgwcjJQe1tOk999XBclPyWwZD3jQNLuJdeaCUHUe7HNyqHaYRU30hxiWhZj4oZ2OHp0XPAxtEhpFXNURqmt5ItF_zPk7WtBdXuk1UQPfU-BQ92llDykWkv-exUqBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olpBGc-fozdoucqAC7iG4uq2ESPVo-lhmFCu4nicBu0MpUNsCDbhoxe_eq8kByT-P2bmfzPxf_eQhGaIosPlJU3bbRfgBE-cVHGIhrI2jANZk9AnqTg3UwtbZ4evP9CfA4OuSa7IZyQNQcEtR8Sz_bCJX78o7k86DlG5UM9yfaq4z39WDF8SQ_r00TKsnakQsdLFVkvyhmtcek236oxINTXQbp7Z0Om_tPNTo0LVcbheoPaZ_x9cifdLSs94ozxP6vB6vuhDc6xvW6kCRUuLJSVaJSSmAruAvmSrrd68YcGhaFT1CXp1_6pkoUAHAqCuSO-DcNGYPP8yaNNoTKpaXw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=aQA3Hd4nZzMjEftW8H5SaXNGcntgDn8vduW_FPRCXiWcA3kVyxnauVtdQIFyR8B4aqGKjEOoNm5nUR575CPMkrirD73wJ72z_XuqgLLApDVq5BH5LfPkGbiGw-OACar6_16ZzB4DdnBvZdG6XFd3lt6EDJ1L9COSDpF4sLt4QZGkCb_dIwUfYxa3v5D0HPEGz24ciT4Wkq7tZ50u9mxJ5f4QanlINXuzDXvr_BBD89EBAZRCWG68M7EIKcba0KlUOuXuXnJ8aH1-L5biKbe1tDvQkXDXs3jZPJfTD3EGB2g3g4LAXgp4FWpFhP77kSXog8ZCGDLf-eQbikttiuAOQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=aQA3Hd4nZzMjEftW8H5SaXNGcntgDn8vduW_FPRCXiWcA3kVyxnauVtdQIFyR8B4aqGKjEOoNm5nUR575CPMkrirD73wJ72z_XuqgLLApDVq5BH5LfPkGbiGw-OACar6_16ZzB4DdnBvZdG6XFd3lt6EDJ1L9COSDpF4sLt4QZGkCb_dIwUfYxa3v5D0HPEGz24ciT4Wkq7tZ50u9mxJ5f4QanlINXuzDXvr_BBD89EBAZRCWG68M7EIKcba0KlUOuXuXnJ8aH1-L5biKbe1tDvQkXDXs3jZPJfTD3EGB2g3g4LAXgp4FWpFhP77kSXog8ZCGDLf-eQbikttiuAOQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBo--VI0JmAgWrwC8XAZZG6pN0rLNdV4lVcUTahrFanyzKMX1XzGqsJa8F1C9hvJ7QkCDnAcSEJLLlDX-i-A79Snnqt2YK_d7j62ZhI_Z4nkXeqdUbReWIyGCy7PivJfHFhl82CZA4jp8_eTHOrsitVZNsOJbiEOHTqo4xW7uS08whs68seaGJWS0VoovljIeXcSHBwvjx0lg_nxp7GAun_tvzUQ3whrqgfPH7CAMN6MLpUOEwSYrcmoTKPpa4EdktdV5mzf9SSTNVHLGjCSxCqszXkhmV7ViejHQxz0-vwIloha3d3svNIg4T22P_ziLOH9Ux1WwoGeuvdX_5K-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=sQkh1ovw_oVQgROmVTP1pPo28o_PWXNEKS6BlkloeS7BF--PCXXi99OgwLmWUC9i1iq3Mr7pXEjzc8SWCpSQs-l5pAhRt6NSZlTDnDkBXukUOg1G6rwKHpkV0akY6cMOGDBnpSt3bXcMmZRZ4dgLFVq-MTf4no1VnuTTaUZNktMkcT7F2asR1tdFnfczRPyr0OotY0duw4ue1Z4b6oi5bLfMY95-CD3TZSL-cD8YoHXxQlNuHdGuMgcUavd-VsYhrpN6hU1lk8NbldFQp4GggK86oR9CRQXQfAPuOnf684L-AZanl58hivUQArX3GyCpJkh5PRBEVJ6ew6eltFPowg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=sQkh1ovw_oVQgROmVTP1pPo28o_PWXNEKS6BlkloeS7BF--PCXXi99OgwLmWUC9i1iq3Mr7pXEjzc8SWCpSQs-l5pAhRt6NSZlTDnDkBXukUOg1G6rwKHpkV0akY6cMOGDBnpSt3bXcMmZRZ4dgLFVq-MTf4no1VnuTTaUZNktMkcT7F2asR1tdFnfczRPyr0OotY0duw4ue1Z4b6oi5bLfMY95-CD3TZSL-cD8YoHXxQlNuHdGuMgcUavd-VsYhrpN6hU1lk8NbldFQp4GggK86oR9CRQXQfAPuOnf684L-AZanl58hivUQArX3GyCpJkh5PRBEVJ6ew6eltFPowg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=h1JVbskH_yX17GG-nX3sRZxsBIo0alvlmAqBiU06sgOfTiBPf4zHraLWfKXvldekoS_hLVQpzjt9EnRjR_42g22C-V9kwIAn_5Rh2wxJTWLGSQ8JyAAZwYCjEE7tjjG2ZHJ-qHSQDvd_HUmQzr0UB0657Dks_2ZZodUxdl0xyDyxd5TpxplD4170l4O-7MvwX1V2jS7p2qbqMxynDqV8gkbp_SD2bDe8Atn0kzDIWEoIi6MrnKjR4xlti2TLSBasAlzdI-Vciv2pGjVgctvZq6nRmO2f8Im5TZc7tdn9IFn2UTJjgsappcL_6h7IEmpCOL3VczG7pXdf9N_CpCLkEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=h1JVbskH_yX17GG-nX3sRZxsBIo0alvlmAqBiU06sgOfTiBPf4zHraLWfKXvldekoS_hLVQpzjt9EnRjR_42g22C-V9kwIAn_5Rh2wxJTWLGSQ8JyAAZwYCjEE7tjjG2ZHJ-qHSQDvd_HUmQzr0UB0657Dks_2ZZodUxdl0xyDyxd5TpxplD4170l4O-7MvwX1V2jS7p2qbqMxynDqV8gkbp_SD2bDe8Atn0kzDIWEoIi6MrnKjR4xlti2TLSBasAlzdI-Vciv2pGjVgctvZq6nRmO2f8Im5TZc7tdn9IFn2UTJjgsappcL_6h7IEmpCOL3VczG7pXdf9N_CpCLkEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZE_BmZQyHgCK5faIDlH8LOjvfV8PHEtcDwYAzpfj9dFAqBEq8ufNvJ4bjq-NPSB0Oq-KSiD-CUIDvQyfUNtSztWzhACcbAHh6lusOWOymDQj8EZQp7DL3nku1-mw8-IWFOprTvRbPkl_aVxmqgarfZu593wdHMfyGukVE-HjBy49R7LvP1Tz7OQ2jjH5LGUJqvtA_AS7wTErHllm9XGM8Pxi01qQYK37bymIMC2l7D8cWvPH1FF-40TchAOxwBMnRv92hsdDAgRprTBXyv0qQG4Z58EyPTcf6fqDJn2UsgUWaZ5m4GvC3lGTz-SuOdQgB9Y3UwOw96oA05FDQA6Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBUzWM5jv6YWNN0AY9bEd-mEalUDnf6Z6734Do5BBVf6H1abhm1C6c-TA9Kgqhqn9rsnXrMdX2somsiI0Ux_6oSb_LJoXYcnmXacwL6SvRqSi7tq362jU7ExorPCGfUrENrHKg8fykGJY6qg0cAB5lS2kGbIi1IE5Apqo_LCm7njMrcpZtCcY6nsN9TKYPQy9J5SlRjf93XUWnJ78x9Jw8sjIlg_oC2M7Swjv68Rp_tho9_quU5N7m2nHmHFx_eX-bYqmAnleJVTypDQrztlhy_Q6vnRpMxSrFb2BGIhn_oaahqf6smkEOg9iBepsDhSmBevpZjZ69EMIoxuvyRMCA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=J2k6rgB_yPJoNp4Vt1nD2uIx6AttQsYnO-p6_f_-_MeuaxGkYSVBv6G3X6r94Y7hMcaBPY03Ym9uJpSJ3mfGA7EPib6SLy2YsSVnuGlfw-3GlhPIHPg-nnZ66X0g3RfeWamsSW0pMlsseA17oytATJahgFrIRDVF-_m90uI2VV0SIEVJPqqWCR-1CCGgnViPb-rOHZdbIdbh5FKRZ5r2tcmLAf5JkJbSNZi23siboKzUaCxhlwd3btohmL7Fh4m3-8mJ6UxRthTInlskPwp4H_Me7LAl7pojtxxIc2ECW5D3EgytU0l0U3Nyuv4pvzhqryZCBTzsdWANwqBtatxk6i6pXYaHzNRukP7cFsx8BwVCCxD28kpDZvpnD9btmEPMAaqAclCdhsgQa0oDfukd8_Gb1Fe4ZALCfNTWfBrzjYEica3uhZLrl89hgxTR4QiLNs_XsE9tyz_U0buJcAvFLKkX7ZKDQOvbdAaEouvHgHnEs61WE0MShk8dlclWbxwP3qqdxZbCPgF9COzGyZZaxq5gfz3lGzvwL5sHoh_V1qLonUimulCn3bhukyY8bhhrGaXG7iuIlSlyOp6wjWrQtV7BMN05Bj9TPfrP1mcC6Pi-rqRBgu8bGqcBj_CCCc0FQ-lI0g3I2nWEE6tpMqXxWDqJMMr9qcOr6a2Ym5vwSTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=J2k6rgB_yPJoNp4Vt1nD2uIx6AttQsYnO-p6_f_-_MeuaxGkYSVBv6G3X6r94Y7hMcaBPY03Ym9uJpSJ3mfGA7EPib6SLy2YsSVnuGlfw-3GlhPIHPg-nnZ66X0g3RfeWamsSW0pMlsseA17oytATJahgFrIRDVF-_m90uI2VV0SIEVJPqqWCR-1CCGgnViPb-rOHZdbIdbh5FKRZ5r2tcmLAf5JkJbSNZi23siboKzUaCxhlwd3btohmL7Fh4m3-8mJ6UxRthTInlskPwp4H_Me7LAl7pojtxxIc2ECW5D3EgytU0l0U3Nyuv4pvzhqryZCBTzsdWANwqBtatxk6i6pXYaHzNRukP7cFsx8BwVCCxD28kpDZvpnD9btmEPMAaqAclCdhsgQa0oDfukd8_Gb1Fe4ZALCfNTWfBrzjYEica3uhZLrl89hgxTR4QiLNs_XsE9tyz_U0buJcAvFLKkX7ZKDQOvbdAaEouvHgHnEs61WE0MShk8dlclWbxwP3qqdxZbCPgF9COzGyZZaxq5gfz3lGzvwL5sHoh_V1qLonUimulCn3bhukyY8bhhrGaXG7iuIlSlyOp6wjWrQtV7BMN05Bj9TPfrP1mcC6Pi-rqRBgu8bGqcBj_CCCc0FQ-lI0g3I2nWEE6tpMqXxWDqJMMr9qcOr6a2Ym5vwSTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAJQHfvFPdswH2OswUbd_pNxSQWVJ8KkGRkLL2YM3v-U3lxwEvPEA2pSyfbQHG3-Irog2ptuCZxDkAbRqFDO-cVfZccNSMbWbVZjDDBTzdzr6_Oj7VK6Hu32NZC7Dio-_lB9ctXmehg78L30lImqZkMRsVwIq4RA7qiM0Eptl1z4bEbQpIp8KZ-_usOpKdoLv3GGJn96as2OvvQdL3B8iIp-EzdU6v7ME8wPbJIePBYVWFX80WVGxT5lKqFrR-8mRZXYMEoF7IeuJecZbiU0TDBLaT-_yDDQt0vLI_MOZnSyP__hNp-EX73wiUSQTlMkTGSJNkatJDDmNEC1r7BZIA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=tp_hzlmnRwp8VmRJSakPW7AKKNaqamRIETf940MjOflzitndzpNV9WxKjGEAkRJox8SIu_uS6IycnCOOSb-WaOWPqdRd_TmWECo-Q7H6pgzft-Svkjuju7wgW73DPWiD6eRZwpJwT2-qo1Be35yr6GjnCRH_L3km0NrOE5aCnq780G3mjjZZ9gu3xNtdWhiKEYJmrWQVlknERMCWCjT0Cn6D_fQUd-XxMXykOXHJWn0QwfEQ9uphDh184s4P1WEe3YfP09F19b3JgMgT7bNJGrOFTo_oXnIXF9HUgwPryKpZ_ebRS_pBzBBN-dRpXisaQgRaFi7Tb_KrX_TDQN_f3LpXdPCrkC7z_XKXmvTu_pWZFzi7UlIwQNKoNbw3aIHjm-CVi7qGLVaJ7_nvj-784y9UzotUav7j0QmbsdcGNgyqZP2YPAD6SocGDnXxwzgz99Aytum1seNS7AWq-oZRUk9M8FRrdOJmz1ATnUIwuOfobUN5VGwFEfCRYvF1rR0RkzUyoF_KOcpicxf_lhX9omZINXJONp5pmQQ7F_Zeb_6LmupXHnTtyzQyb7m3Sq3oToeOSCaRVdcPlwWXOkgiHh8AhWCXWqwvPmRuBcB6CFkbHMjO-aVvIISAO24-gVTHw-Fa9nm55uGMPnou3JlP9nTbA5KZSqOsCTgu0ZzAn2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=tp_hzlmnRwp8VmRJSakPW7AKKNaqamRIETf940MjOflzitndzpNV9WxKjGEAkRJox8SIu_uS6IycnCOOSb-WaOWPqdRd_TmWECo-Q7H6pgzft-Svkjuju7wgW73DPWiD6eRZwpJwT2-qo1Be35yr6GjnCRH_L3km0NrOE5aCnq780G3mjjZZ9gu3xNtdWhiKEYJmrWQVlknERMCWCjT0Cn6D_fQUd-XxMXykOXHJWn0QwfEQ9uphDh184s4P1WEe3YfP09F19b3JgMgT7bNJGrOFTo_oXnIXF9HUgwPryKpZ_ebRS_pBzBBN-dRpXisaQgRaFi7Tb_KrX_TDQN_f3LpXdPCrkC7z_XKXmvTu_pWZFzi7UlIwQNKoNbw3aIHjm-CVi7qGLVaJ7_nvj-784y9UzotUav7j0QmbsdcGNgyqZP2YPAD6SocGDnXxwzgz99Aytum1seNS7AWq-oZRUk9M8FRrdOJmz1ATnUIwuOfobUN5VGwFEfCRYvF1rR0RkzUyoF_KOcpicxf_lhX9omZINXJONp5pmQQ7F_Zeb_6LmupXHnTtyzQyb7m3Sq3oToeOSCaRVdcPlwWXOkgiHh8AhWCXWqwvPmRuBcB6CFkbHMjO-aVvIISAO24-gVTHw-Fa9nm55uGMPnou3JlP9nTbA5KZSqOsCTgu0ZzAn2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEa7btqVz2FFa7xl_rIxnJC82iYOxEpOyIwtHN7Ttn6sZfyWayM3Kbc0NGXsemhUIZCXWRqfNhHF58PXv8YRvSxa1KtEl6-1KU0t_YGABSSjZmEX8pqoUkL7s1s29ajGx2F3JiVeOW8actoYNzaqencg61_GyzmiHaUB0cLC8vrHX9pbckGWf0ZqhVMRXKUqUa4skaQ9y-bIYRwC9HZzuZIO16F0cQUuFsvy047_znsma4Uuj0-dJvzF5GBS4uJ3PtBNugmVgzhp30F7-N8oNmbtgmmuUjQKH2LcK4xVISqm36Eg94UNyPmb6xob0O_6szyyDFc7o_C9XfkaLR_QZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQN5Ehd36CYCcTv5ckNb-0kIo51HsId-ZXHDP87HKVvql7HnCC-bScdU5scxOgKzA3BKe1axCVsxcVG13JncjmFU90ff0i3kTldGREZICwpcDVh6OPTWkIVoy2c4vG8YyeoB7bAcmfvUO2oQ_w1HCSUKZ9e2AKvNiC4I4WerIZosC6OFWJ1Ylox4joCgfIrWGWNm4UKorFLi3rP4gnGzO4lQ5uSDABk6cvZtFlB75dH5yn3VFUW1sfYApIOguuJSOss2fWW5s3KbwORIxcn41JxUBCxGXi9QUiEFPHsBYV8EvPLM7XAi_wSS7P0cGvwmEx2riCRVQSF8tD05EfTvQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRzg3mKO_5BzYsKrCxsxjEkpK6-W5PfvkyEt4YRh4evydlLGB7FGQvoYyflGNJQcHc1ecLgI_tdbMUqILE64cGzoDGwr71YXmvxCUJ4xHFQ9CX_rA0VXV5IQBsyrV8ueTMwnz5Bxr9UfErIIijGLancJ5ObREKZWcnN8c1LAMCO39PN0e0C3vwcz1bOIy93K4wFqkhTDaXO1J4hgwxd1llfhs0XTYNI2kh_lSE76XmGDtsAYukwm-pCzZ3vUlR_LpPwnHjA4e-BthR3VBJf3OAL0ZFMjvy0PcH4_kSU4nclwIj8KAlhhOcFZsSLw5JmphfDsLOVgOAbPwX40xfLd5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-EdzVbBJ7XgSENW0N_nJklQUBzf_bseazfx6bIzBlOYVQyiTWqL9bJycQD0U7ykvH4thLXw9qqS-B5u948PEFvJhXRwsO26dkaHpoGdPByiMNYZZ6SeaQaGJb-WdPZwlZ4qKGMXK0ByFnyedxXek6DbiAh9aLftTBrXRuQQhzO_8lthHCJupZiDPG0hMmjv62tG0HID3Yeomy7HiBHzeFZe_dZNYTkputICl3aa8lo716NzHzUf5Dg4a4pekAVvHqik_ClYQHtpCzAcOpLgCL3GcZIBJTalUBiCEpFYZ8yMQttnh3lZfH3AY0sPvc7VNZ72DpQJ6eq3KxMBmgvy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTiZv9Wk-88U9FOvTyB4OFjNm_vol1-dVOWa59Bu0ddc1pQ0WNc8XSQhjBLKIorBqDdUdMSJ0YAGfpf7-eTCtDSHnGlk4GarUQ2-tSdc7JlEXbWObD1KFsfS859ovSBdeCLQyXrXjX97Tl6qkoOIj27oaN_m9Ce_k4MxNWMnhGvyhkoSFDcU4v1Bh-Prc07z1d6EpEJKFERsWMreR08oYF5DhnEhp1xqdjDtMdWcKor6-q8gjEtjxmRWCwMNKn0MmiO0Ztn0Ju4SQ3wn2LR2LhcBrFEgzuuGuYYVWIdtV3JXKcGPJzAa8TQfwhR2woO2-QeL8j2BOcpOc8HnTmm40g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul6CTOJK1FzXMdfFE3yWkuseFTqWPDXHaSNypwQRxeGOz55qbQhgPl0FegN13mfinf6clCNxM9p39wj9mIS2EfPfag-gyAZt0B7DZah8KnHzl7T5q895XA6TmrKTiJbPFVcx6cFPY3XJNhwnVXomgTepl2b8PNuLRE2b9bfYcvJYl08SKZU7dRyavvil5_37plbWtZri5Ab6o4qsuDDZbwDEFqUnEwnXGzuxibBadbeIuYqUppR2lLNKlkGOu5Xxml9JHgF6wk6fkpegT0H5uAEwtuHe8MGXWYe5KCwrtJznKDgj7U6CmsDD93LQuiS8CLaAEd1K48iXxsDn5QoBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvhpgbQcT4-0gnnNjBYRPmsfMkjByQQI8dupC5j_hzWjHkK8oGjaFVKisbrMSH5Zf5NMZrMwu5lshXPJnsG8YqHvCVcmhAkLXXDAzQon3KDtOXoimXhWEJzIWvNV9D8m0d3w4Ysdgk_1msd37b290lMnrPOWK4ZcGRKk_D15q2WEsSyOXuK-mcKWqaRKl7IWAjT4YLGx7Z3ODnLLVmeyBSy6U_Tu7-fjF5_Wq7EuAHDajKsdjTjVDFCMr4ytxZ3tka_1LJk04pOuCl7Iufi04foXdnuGFA5xcjIyUV_VAi8YAHaXax37xU1GCeL0VnaZw3JrnbJPRnqAMd0SC4GTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxNbf1zoJv1abweZqfX85q2szKSWMCj4prxI2tSEKSB-J5g_qpA2bbBFm12vPzyLvFl03Cdp90Sgn25FXTSUVIjHJl9P4TQl5ET-_f6Rz69ixyX7Leb6rrZDgp0VeLIiyeOzPEFSJ2N1BqOr4I4I7zhO2NDcxHtaYjFx6kut9aC9rfFwOBNaCzp-_Tqdyga9J0QN0mS25ENG1Lx8VFr62El4zA0wMWITvPiev3JaMrpu8TMgKdVgeg-_LsmGF-MlhF6w0BZf0HAXBWRhasHlLwuiB-Lw2B522ET4L7a569yvYU5WFL3-zOCNk80TDcN_jtCtDJ46-TIxgELUsoWjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNteI5JGP805Pv8OcAXaasDMLRi3vtb7Oe8NSEwtQK_3NMtdwxsHiFk1MIfhS97snliReCFn1mkktK510RhbOxf05IhLjhqbFEe4GPB6ZjVHEGMKt-_D5seTVi9E5bmCw25-3KLVfgWlQCaD3H4VVu_YqueKzvpsjycsdwOdjhJ7xuJCdUE2fdoiFjSWu61bN32PwDKH6e2_jGn6vwDK6f9mmtYQ_5Ca1xyXDLdZb9bMF1tcMe7W4SuEMXdsCMkoJYHxr73i6h-SPIKeO7CD3KpG6gxlsXrfYX6beA0ov1W8afGkUl8XmZ_AwblW6I07hRzyywlqSBdUm0R3MUmEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCYlzBk_SwMV8msmTmMhNinNtT5EMkIvrqP1w0c-AbLADygGcv2pO-IG_OCkhxtCGZa6g2m7E0CPAzc_sQSoli_X2acHTBEi1ERVopXBOiNnd1lwOqVlP3EM92VL-EdGRbJZGyZJ9ZUOu7VKVnPD39THH4SlnFZHUwQEGzxjnWXw82lVR5_Y9WeM9QeRCGUJtQpeCAKxLKkP0-_Lr-RV7DSc4K_yxg1Ui87Fl91SjgwvJaWotuyZkzF1WcuXHusiRoOC6QUpVMUyfgZ_jVF4yvyzW2GjY3KTheFb9COwJS-EcPtjIsWFspR3JIGENNQddwqX0G7orYNzP58zqGlz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQOdTJqTGe56G5CbbPX7Jfho-fd1t0llOAGiI6ajJAqo1J-23LhpMQj178p9AVDWB5ctbdv_xlmX2dx5iDLtnMKCxCpjVVJpQf9lLB7l8C5k17otrXZzT-pDduYV1h4y1J6rdehVTuvuqmOTv6skvlkePn67vWqxQ_xsAT4t5F12LdOCTzBbtcwmW9yb-yJuZb01rzEH8r2j6PQ_hQjVOAJMDc7brEWCY-AUIM2NDHb7kK3juEtpaPYjgNz4sKK7hxfQYVoC-SETl-nk8y0tNo-v2frJxejj6YsgpnJfXNn8G5q59iw_n6uTo6fAUgtRHOKiTyH6iPzS4mvShAJosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dR55HA7lJXois6Qsd3iHUHs5Tgp-ipMm4Yh3ClQQIfMY9V6-tmZzXSwelWbxB5gK5Cahs3wf-p3OEU2HAyci10OTb08aFSpkYCz4qZgcLCSaTFlVslQqJfq5qsJQSua2SNGHLK4sK-5aJZXEhw_S91syM-Ys4JUX3RlOitjpK3kSl8QQsx4633zExMeSfwaBcmU-PZrSGXuhi5h95L8M4iPPGHMTj-5WQhYiTZXHJxH5EuEIGxOaYRV_mE3fk567mJkDMAtyM7UHXvt5iK_uE-JZgiBCtf01myudECx8ioDgWXjDtiHTvEkkgpLMFi3zTyOJz-IoZmlPuIZmtjRlKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu7r8x9UEVtSZECB8N7mrFSi4XhH5LBurtYvybJ-eGWyzgUzR0inYDpuZDrZnnLZqCkj5nHk9OC-hqesKRhXEmpUcALUl98pmItY0BUP7lNP9UA_bnU3KCwDkj0pA3r4_3fDwYiAdwh2QtjOIVYuA2PdJ4eoQrJ4oczKMO9NxQ34uFeaHDp4G-YvTM5NPNn7oOK1p4qhtza8yNokWRDKre_Bv2yH53UMIUSQFPXoH8qUY2cLexQotdJMZSjwEcz8Y-e5qNOjnRJh9lFUZYxbFqEuBXdHZ49G-iz4PLPvf41LUBfEnTOFv4BefktIdCeYxAtrZuxP3hKJCNjMQncqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGYCd9XIrJoWtjgUwFq8au4vrxeoLmOl-cGGZLa_g05ZbPpmBwaUPYrvWB-eoydyCk5554KZOLDVTsdPIRAkYpaMQGUn2Rz3tKm2-vw3DVhh1Milz6HBOmJ94sLj-LbXfG3t1KtKvUi4FOwd5goxPAFPa1ns41CxQeFBW5u1AxhlBjJIBB8twkiT-xSxg9q1D-5DtNrBeKrGt1_MGEac-kR-SSsVUMrUAptUM8YhxVRskDKSLxhhdvbh8uMcIG6l8zhptSxFoP0-BuW4K2KXKGWwkS-b_NPqSQb338lQKFJ3870IJGhqAmrQqZEkCuGWoYpGkIMtuEuWKn4ovno7Qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPGo3gsczE97lsgRCwt36eh2z_bL4cjaY_QiugzUPNtw0WiJi18JJFhymjDqCyz0cHzhh-B1T5lip0NMvRy0n0so_aXInF-q2KxmBQw7_EWcKBbEQkpaasrRpwkfmdrRDCmU92cjQZKWdFErw18UhuM1SNQYq7OxYa6U1qUAENPRSFAIveofu_Slqy5kTMwSGUsK6BldJYOM0ksSgK-b7CWOmaKT745CuFOL6ccHfjdGdsscsai9V8zE-oEaFz8_49zwClltAyILo6o_AVvfn_ufHtS4gTk4Wq27X4kRauCZvjcPnVn3vecpw0gF1T6McrB0LV9z95I82T0EPilUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia50mWHqKN0dsot9brOS3-7i1qVLgJZl6i4K_jr5ppRjd3fHAjoV6hTCu8I-HJfoKGi2s6iB4e2I1Q9rgSuj8AyDBta3SXtuqb-P6Istb4E355qQfQKW_B5hc07ME_6V3GDYOZJtbQRpsVJwkIzDUlCb2f-Dtp7FLX-XkBUWJIT_KR8P8Gpyv216r4i2HUGwY_eYWoOLY7dIDZa5l-8fL1QE2c-MR6KAEb0E-1qIucFkrcRkXNKD2d9vtu_NofGamzi6nu53l0p0-cr_N2ucl8KmHZBAKdubp1KnfZWI-AuMfp6rqq8dVWF-5N9POvve63xjZovzgwM3yXEDcdu7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qV_qiBObw4tBzdRVBTcHIePPY-oVRrDiRQIqVC1kvKLBi68q1XuOou-BCxWvXZgc0tFJ6PbUQTxGEahHJUaEGFHxY3KuH2IQ3FB0-GlAdnjk8bviFB1mT3qaHyrHIiBZe5fy9fXCRovdY7WrFgVnBJeumKqgq1QA5RAVAbU05guZrPYkvomvdD8Bq7YVTibN2Ny5BTFH5j-xTFGAaj_Rnqy6bCGN9GhJbDNGcgMf_DN1vx85eFCAf0IIfJ7XiwkMddxE6awomICmg8vOjWuHZ8WM0oZgIYnANhXua55Xu7ZQOBBXe2wYhQnOmIAc_-DGwDzHNS6YiQGHgRntfPzHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlK6soWdvERsJfD94tP9eFha3_0R89EwtSiRZT3jl5q66jY8KTOQS1WVKZMkiHiYnBO9wtO4sEpF-EJnAgIHFyvK-UJ2tLlL1__iKMw-YX0tw58oooE0Ptp-nuxYjdvxg1vm3Wg3RrF1uKhPrLRLw6OeN5ldWWNrJL61XAPvOcpWtxDZYvgq9AVcnI0URmB1QXcMdoWKxaYFtHiM12lxwZxeNBFPPhwz0PF8DEc1Hr_LQsPOndlBu0_eUhxMyGdg5TReNHw3mxw46FONpnDSNX_k8EeRkz98x8R3Fm9Q0Mcc5wC0gXNJdyIHGctnVnh83m_pIGXf4iVf0BNFGji9jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhvmk4T65zZTIAmTfcxy0_dXiMho6BFvkrGRSqh1b6PIr1PAcVQMVUSuaP52Km6efqnq4oNZyZawJE7PNSW38Dp6pmXl3x3SL89DiAyC7z-pcyppAaHehUMKO8x_zfxp-XdReQq0vu0pkeOqiRHXi0MQwq5LMMueI6UOo7BcE45SvoueLpBgLC2fDzOPgebPDUTG1Q0fM59mz_Zeyuhgt-oXRkB9lvww_8v1ZexLMNIA9fP_EEv0tksjWZqEeeTnK8lhCxL7s1GEYgeaVVP9M8sHo5ypfZ7m96XiXnusbeQMslqJcqR4OA4httlUsQBOtKCefq1xQt1CuxNsLT1gaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyPEEa_K_YSrGQIobO7OFSNA-_DaQ-vk41kLP3HOBiKZ6AK6WDZcQGoqwm-6Wg1COVIfHuHY_0LNRDGpqmMF152UVzUEtrd7OPVp1mOjIVjm7kn0btbQbPfypu5rJO2O414ZRWsaQnz11_IzYwt4lRZ1i_eO8tdzlGVnPmxbQ3igjjZquQaTs3bvXNoD-nJMiqr7uov0uubk-LZl7ad-6ouRcC8o2lKfUi9nar68fbYeEz_uc8yJw1LRY8mKLZQb3gYKndJnyGNPtfU6_9XfvWczMdQnFEp9VHDk2H4_d4luS2JQwZrDEpx8UXBKQwYI6lBJ18kftuL1B08LpaQ4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbRd1nfjhwEwXeSzajionEc6wkxN4IAjS5OHotbMW7ed37qYANlW7v2PupafCz_e78b8OSG3-DvfY-YTxF5Fp0G1O9PpcDhGtfWsdIqJ3a-i908qtanXB5RhD_MmylVkyPfxSWO5gklA2Yd8wz_W50ICcqxHa1ldMJhrDmnQyZ_lzqY9Z-ugmxrCnuSJjSvdtF34X164VunEhnZp0BOsOIYkck3lHD8jQr-Nu_pf8rtqf9zhPmmpJvWJ19AcX8oiy-Q2esNpSQQV5KyzYWRPE2WXGsF4NNJB8_JlwG4UOcjfvkO7xAlaZ9jE0iYnTI3jrYG2A8FsrXlGmEzSx36RJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1ev5OavNtlJBFDkZy87FzOu1veWcQ8uN48eCAOCqvZPbhRxrYjINuXX4-xkhCyIHMuhkLFWaqoF1iby6bEkgWrLwwf5ckpq7agRrQ-0nxJ_Yk7EX_qDFvFPbKn8-qcy8G8uNg4__sklIiVxfhN5SEqXfwzh7a7NlaqFnKvaz9GxS0wXl9hDBHlUxgHtyJxG_jTrh4khHWl2jSXkoAi607Shw1XrHu9hwNWIt2NQUXv-j3mOALtwogu5b7KMFbke0Fous0HBzAFpL9WGb50fK9WKm3tvVLBPNBud6hyfRMn0GCvBTM_CYP_6UdU6RPIYw84RfDU0CfC5fSrs3jh6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvkxoWMhEqIlwW-wWPRelRDWi91FmMDt-cVVvnUOYQUiXgY500PDQPyxyeS4CB6UJ-whDjlVLTDU3vQYBgLbeyfVewzKUgdVqhik9VQiBWuBztye1Jn0r4kwySUkwrL0s2QIslrGsmyn2vwMytYIyBh6WxHqLk4QdijwWyFGSUAga7HN07B4cAe0ef2Y0MkvJK6jD1zdemSQPzs9h3t1bveA6u83s2rYX4pHp2bZLDlIZQyxgHwQqUP4kFPfJqPmMiQNVqNKDMIqs2rr1bFhD3eBpx9sdUcEIobDy0NW10nxP2my-_BrMVOzFjr9yN5sgnkbe9g_ywDawD8zWNofVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBU37oMXWaGEBVpyE4zDuEm5XnplzzeN9SNDtX4Egs11Opg-0eYCz309n9DzwX2-_xEwQc_X4k3vvqEyIN9QhZNxDCG0Ug70TQHS-jlDS22NVioS_qFlmKeUeWTmgdqhaLIqUIoZ_3fz424-brums5J9qHk7SLPf0dVbK7pc50Anoee9008f8mW8wtXJD1s0Q9llJpryr7vBbKb01cDKdG4-tXox61rlXMXn7EBR1ffSBHsZeAkMz4IEB1PXcd9sbYCIRVpzgXAJjt2wpZSAne7bQ7mabL0LVOZrNhvm2F1qrHYpBm9ABh5TB5yZu9R5AdIZakPGHaqYhsOlsV3XxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZK5rYWGKriZHRXykI985TfOcG5HQmR5uxrMECHUia5iQLUpFoQxy9CC2czk5Je4FmcvPWqRPCvho34xlKd08mCVgT4uDELGFS35JwNf18SNVnoxdbUFb1c5ESQ4SHWNhKu5HC3xzyVBQigISGGN8Qkje_V5KrXTvgiiXqkRxtUSohhMNpHVFmzDR83TozVQ5nbswmpHUxtvjfBrEM_sGZOU-24o8pGJIPX1DqYabA0om37eVVkjTpUta3ASPMoi6Ric9IK668sjRrzj7xEdQcJHna6VXsGIPpoDWOgAs-YmcMwdf504TXe_Vnx5KO9af7ZNzD9CrLMFMVUHQhQVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgCqa2jypw0n_PYrfEYZFs_r8rcFplPFvqNUQnDdQCyD5MEQaYn6qD7H0uviEMr6l2T0G9m4IcORIkXROl0LQAvx3ELjzD3-861kphpgSq3uns5GktgdIwbGy4KM39npOU-_ZDeQ8Sa7TbEIlbL3P5BPKXOYEcROj0yplpYptsn0pz0obKPRIBk2_Rt2oAYxn5SNKsAsWG4JPdOmjR1T2MluhdAEWsCCOIpNT2v6GD4mGAD9rn2X2sEwh1nZOu6o1hCo80v6Pzv2bMsLXNOwyyUj0sEkOkvhokg6VUF368tvvvmWvwz5mozcFgtJLhhCWtB5xvk-gxIwmidwm1vZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSmxRLF3KMSr2AfJxtU6ppB7Zy_f0BAzct0L1VXn513j4i7gUModC9rjnssOVMkzhp-GLCtGnSTeNQHkwFjff3PQfsYlcGt0lSfnpXlaxat8QrlaLkrrJwi6gaw8atwFfLXM_Gu7XTEtRxh6B4a8IBPqAEYmFsmQR5wXTeI6Nl-S8ANseSs4YsFKTknSQ01gq6gnMSgY98eoobi7oMzHTsQ6k22OkPHGSbU8NkzrdL_DuxiW7lmK73q5yk59RQvjdxbVEIRS5zNoWufAiuUOeoIDije01lo4Jj7Z23bpKP8ejlAyvnjhKEdkjSIbd545Nomvcmn5277x80R0H55KIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9P-IINBpggpifU32FkOiNFlXKYciWJlDaygXfgFUJCdP0MU1SO5jfG5ui6UljXU05CxeaULbw7PaGh_3sTI9D-jIq49kPmIQ1y1-uive4gEjjbHx5eozBbmeshyi49QXeWUDaKqzrKkX_Q481BVepScW4ajN5J30tNKavLQPf1WBHdZL3kd6LTohmbgtpnPiKLg9E01Y9V--7nBALrMfTUYGJoEtUTU9-0dH-H35n_Mp0bLoWCKSQl-u7kIkS4FGqzd9CsGHy80HB3dLeYncm6VFASgiUEDuKgeONB-5BvIycH2Mi3vUU_4tQbaBVmtcDNWENR-KPTw3LGiu2Hfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG_wX5i59tLVCASsfA--jhxWJbHGM4CWg5hEW2UR6RUhRhrFMJ15U59NH55qWIAFybI1-i0DcD4nlfbD8x9-IVRaFL2GargAwZB7ggke2JG2oAFl3vzQxC6LGytn833l9Gqn0NTJ20zGq4NUJiZSmjkHexghdLtqI0URf1D6ZASvTlXDo1ViffI6bFk3rcMaxIEH0_SeV0doZJADDw1ykxIruk2o5zBEsVuAYB1WsSvO-zHlk72clH5shZT56AgUJo1SUfj-dSA0U_q3Xe42608B7yjk9nmi61OFHIYDijyPRtWrT5HlAOqw3-kFFeWYxIX7VqjOAw7JOJ8iBm4IRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHPePpmEcMl_TxKlToCFprpLbW-XFfZ8oQmil_46Z8YxSr5bdh4YngRfh_aV1jRO1HAgchuc4hRvkwUTKLhdi0rdbcGTAI2Igb7JXr_9wxm5C16U2q9SM5YZu2t55prQdZ-F4Ha1LXfFKgtlwbjJfmTlW9OjTurqynZZVhtUOIl2-eBB-CcqPCWL7J1e61kSfekrgjFna6Ropl44UWo788J2Lg8L1e83fsI6YWW4FreChECLwQ46N-75pqtSXOcO71fV0ZX1gIqZI02Ll-KwOvrr42duveEeBWLGUW7ZhKMqlUTQ5Q0JVEN3MkJnJIPa_0VBLfhDkIR0IHLRgPjRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
