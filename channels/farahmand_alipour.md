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
<img src="https://cdn4.telesco.pe/file/hQXQTtxaZn39OTsE2gWjsrksB0nb3hkCUTr3XplKF87D0pjjHeUrvfGTSAF7FlBkYz_5fKk2FHvt58paKcjqeWT0cyIQRDR7avqaOO772Y51aykokwmbruZGJTsJwlbUkaAZkdmGtzra-QwFbfmMGvNm8KwruM3ju1L86Y9ppFtxByx619AGV2I36EvQ8esybWtX1agk5tD_itLezV4FfSNwc-wA0BEvHyxfJCT6VvLj3kFisiaAn9plC_OH6b1JU9HTdYktspX9HfCKzNWzu6yBqAcAWjlCD36DeGhl2VIF4Q-Csq-cURWUt10U812HK_YNr7EvXgxMpC32LWYAKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 09:42:44</div>
<hr>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=C0ouaDua6uHvQAXUtRmXfZ5mi2wWFvsApQwAacjucjg6IXmBpCXPLelqio4pPWAKPFl9xqrzR_v9qI9-WVTxzXVQccvLnnQ-EiA60Cro4uX-AbpM3BaQ541Dr4ECozZZsno4JyBbCzuAD8tf1pu9-KMQNfv_HAJDF6FUTfKBivp7RCU-HXNvoUBcfjyJ5_A_dcKzHCUKeeKVwGoWXoj0yUA2NZ0lS_L_W_6apX_Hi_sMH4QzjscyZ8ZXJkymGpD68IyYr8Y6ocTc63dKYrjYzZuye_tnz2fhuULFB0FZqtdeWJ_c1Rvgj_EPuzrkX6ufTh-BbCitf7OVLtedAUTGHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=C0ouaDua6uHvQAXUtRmXfZ5mi2wWFvsApQwAacjucjg6IXmBpCXPLelqio4pPWAKPFl9xqrzR_v9qI9-WVTxzXVQccvLnnQ-EiA60Cro4uX-AbpM3BaQ541Dr4ECozZZsno4JyBbCzuAD8tf1pu9-KMQNfv_HAJDF6FUTfKBivp7RCU-HXNvoUBcfjyJ5_A_dcKzHCUKeeKVwGoWXoj0yUA2NZ0lS_L_W_6apX_Hi_sMH4QzjscyZ8ZXJkymGpD68IyYr8Y6ocTc63dKYrjYzZuye_tnz2fhuULFB0FZqtdeWJ_c1Rvgj_EPuzrkX6ufTh-BbCitf7OVLtedAUTGHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwsjJEBvGR6DETBxRni9hGLj983dwGl5LanuBbyPumc3gkO7Osim33tPfNlxC6Br8Ff7kb7mtRP4JC5qvlDqVfacrkP9w7CwP0XoBPzMt3o40KYO015CNakO2UTEgXEyif1Lp58Bwv-PzKP1ElIPotvFTrzrPNZ5cqlTkBI6ntQItpUgzqErayWnUMCRrtXfmkO0v7aGV3D-Ecj-1QOsLPY6gpvxoEvNYCeeKZ_ASWbuXKU8PthQYmO6vIR0ym7qbTRcK4XQJbpIljnf75ltFjXZTKYMOBUgKNfW7jWlQ8VaX1JWj91yQj-2Nqu19RGbacnX88huzAwcEfL6ZKSUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1SdukNYvvy9mfr1Agx1dIPBj7R-ysewpmPD9QNZP27PqkU-9oFvEnvLR7Me4VdkCtQVIcjM5Ji58i23rILMtEOpYtM87TS5hDKPM4CX0mmo57WC2uMvQubaSVy8K3mTVoveun0qZ9Ll0nBy4siOQ66kIGYoEDgb6AD00nst0XyitKJzcme3H7QJaLZGkRpPybYsCW953Kea607TKcnHcOpyOQALGXw35WlElvwwLBbgghISuYkYBs8M3jtPTnDw1d8YQYVjOQ5tt7hbQnJMrMVKjbT0E9tZSBOnNQBTkn90pkpw7y7wDMtR58tQFgC8E02CigC7xdOsKPYydNVixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVZfXl8lZ58EPhTA_1ve4hs6oGwcTaB3e3lcTsxkh5udB_RDIQqhqdgAoFIiODHvTJ0SPufPUby1guGEV6BjWlJgGemSkscePpmNwzAvyarroXsmwxNVgR0Ou_mK6hTGkvCYrAXZvnqnYBmSgk_VLpwnd8oK_dWiGn-uQmT7raYbD6Mn-jPsV9GbEt8bAcmzDGjJGoFFsXlTSQQorvAfciIa3UwfTZ-H7KwekfT7AWUnSCd9POl60bAEgsi9BgfOG5zC3LVeYlAM4yEUKSkrzkYykW487XMMwOpBbVKYK_4hcgBuGZCC-NAbDbwtyFs8FJPbb9yA8Q-4l_lDJ7dr4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq-qDV0w8shy1jeStwRMjipA5gfNDIRI8XMxAOz-q_idAjTng132C-4UArq6B7zAQMLHXGTgBenZF1QKIOy00Em9qsZWRF-kJl94uzcgTKBNSEbPpICnVquRW6Kx8eUc7l7NLMm28gyRakV0mNtsicbYFWl8Gj_OmObqtpEQk5K3_c3scZAvagPdmMIOeKNwkywVNGeiDA42SLRODO9VwOBxJ6rIJXcQtYhFO0JLrXKaEAJWXI5b-9E5I0-VjLFLdN7_HlZCd4ykb7HjudtQ5sl88ltn5ICBQavnQSQntCohyaQVP35vRsxFwfO5Hln5dzgS1juagzV11fzNJYkwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miiLO1r7IhZXHOHScX02__s1QXOxCCQA7vQCZEBq8liAVW3NwWAO95z9W1K3CY11fBmj9dc5obYwTvp7bM_7WD-Ql0UVDYhDBVrmgd5ZrbcjpM88abjamkyD1VyfxX1hBm7UUfLVbwys8vlVuxclRd9EzgB8PJSf_NsBRqurv6UbY4pn8zahbqlEzHCYuk_5At-zNBKOMB9b1YuRGDIcJrMzBlM1yvJYuUu2WMJr169T17ycDEd0pzlg1_uHQb6y7AHv5Km771YFioXRWiu_4PqZy2Aj7lqqGK93CnCDA2t6mMx52DsDMB8qR-ZZctgeGSYE2530eMQSvQImeLhVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arQuEFOjeis49aIKf1pJ8K0TlnY1EmIvF1XXCuPdolpcVJncxJWatkWwaN16C4rpJgGA2FFzKH7H-mz8dvYIxOhbuEGoWxlku4xg7_xO6S8FawH_iCOjownkDHYpsWEXvE24JMjbVSVYGxGNYF1axNzR3TXyLOputLYgfRB-SPt0O3NlepmrudQbXEqEwAnkwYb29u1b-M1i8mkpUZtzqpupdeTAOKqg_Ic7jrWeJZ7RMI0D4ka6JIwTrozG7V7hkEbtNmQk4QaNzJodiXEH-dzWr46Rv3MxXgpDZPp53x9NdII0f6Ax4w7S5QFClo3GIRMzJ94UhxeQXJs9mzi3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=EKmWsCQkWFpcbXNGBBPc53K8DBaBTNjzD9w9hHBxyA0zWmBkNBMOI4f6Fodt3Eu7ii5b7R23TYiZtZCDxwKl4_fSkOs9ncIoUT5VxuRoQZJLxSQaQxTxV0oVRt876nzsiwRNlSWVciD81wUpM15Jspzd9W7RcQOEqj6D38OP7K6VfP3mt3mUAAJb7lTYGJzAF4wvDAqnGMO28kGNYyxVCf6_KyDUvfDSyTqGBMAxxTAEC0L_htoQhlqiZlrduts3YB70iiZ4DhBePL0TktOmMkZCxa-jvdppJEUMHOynA4osZ8eYUJJU9TJiErfb4dJk_WETiTAVMDMvy-S4E7UfeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=EKmWsCQkWFpcbXNGBBPc53K8DBaBTNjzD9w9hHBxyA0zWmBkNBMOI4f6Fodt3Eu7ii5b7R23TYiZtZCDxwKl4_fSkOs9ncIoUT5VxuRoQZJLxSQaQxTxV0oVRt876nzsiwRNlSWVciD81wUpM15Jspzd9W7RcQOEqj6D38OP7K6VfP3mt3mUAAJb7lTYGJzAF4wvDAqnGMO28kGNYyxVCf6_KyDUvfDSyTqGBMAxxTAEC0L_htoQhlqiZlrduts3YB70iiZ4DhBePL0TktOmMkZCxa-jvdppJEUMHOynA4osZ8eYUJJU9TJiErfb4dJk_WETiTAVMDMvy-S4E7UfeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LmsemA7ZMD_x64hqUaDPNjmMtdIfwtYZCITBG2_v0Tdef1AFvI8q_5Rzinox6VCyAekKCfN6jo-5fpYHIuJCia7Uv8vLwTud4VVDNJl9bqDViVu61r7vHAVvyFQ5zxvaNty2APLE2IoKucuDwjMrlm-jqXViJNwrJyo0pUmDi_syPGUeBmS1RiEMR1S0_keUiBrZF0Sef5bSwBA9mlf-yhqVsA2raaH0AIs1wfZFY-IE9vD-gmwY5rQEZNN-CSyr0t4COAQQMRQ6P5nMcDbqovy2byUy2L7SZUkwYVGVvncWSnGattHYtcPsXezR3VlLw6O6Bq1GmZjhrECRCgCvG3Z5NiEXzoyZxFhtgFssNl3g-b0dnXj6jWFCiyUs89c3qTHjIeo0rmhdTdlqutFumnc5WhF2Ku4awS_cTiZOgqwll5Uljb2VFcFZr5oVlBSLO1bIAKUa9ImxpwPd4vJF1CsKWGzvaVRmDv4F6YN5Y2dNDWXHfFCeOYzIwnbo3e_YK-rDVFlA17KXk1mjscDjbeSEKVGfy99qvUFB0Ns1-if_fW1twSeNW2a4eA4rYsc7vt8wseVv9GhvWlg0HYtD_qockCbTZpkLV94pRquaXV3QphnlLaf3dt5yYGibp_ozXl8H-I3z8FT3JhHbjDIa562zdadSL77gzCVjR6Tg5aM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LmsemA7ZMD_x64hqUaDPNjmMtdIfwtYZCITBG2_v0Tdef1AFvI8q_5Rzinox6VCyAekKCfN6jo-5fpYHIuJCia7Uv8vLwTud4VVDNJl9bqDViVu61r7vHAVvyFQ5zxvaNty2APLE2IoKucuDwjMrlm-jqXViJNwrJyo0pUmDi_syPGUeBmS1RiEMR1S0_keUiBrZF0Sef5bSwBA9mlf-yhqVsA2raaH0AIs1wfZFY-IE9vD-gmwY5rQEZNN-CSyr0t4COAQQMRQ6P5nMcDbqovy2byUy2L7SZUkwYVGVvncWSnGattHYtcPsXezR3VlLw6O6Bq1GmZjhrECRCgCvG3Z5NiEXzoyZxFhtgFssNl3g-b0dnXj6jWFCiyUs89c3qTHjIeo0rmhdTdlqutFumnc5WhF2Ku4awS_cTiZOgqwll5Uljb2VFcFZr5oVlBSLO1bIAKUa9ImxpwPd4vJF1CsKWGzvaVRmDv4F6YN5Y2dNDWXHfFCeOYzIwnbo3e_YK-rDVFlA17KXk1mjscDjbeSEKVGfy99qvUFB0Ns1-if_fW1twSeNW2a4eA4rYsc7vt8wseVv9GhvWlg0HYtD_qockCbTZpkLV94pRquaXV3QphnlLaf3dt5yYGibp_ozXl8H-I3z8FT3JhHbjDIa562zdadSL77gzCVjR6Tg5aM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=QXYvXi9gOs08KWzpY5hifYmkHmdX19VGvvo8MM9Bz85GGG1MsNcC5dgTT-rtt8k-ye34b2TZYb-U8OvKUUD82qd2s_dLTTbn4Zas1paQrJVxxQGc3cpa_d3a2w9yatyWjOnLvo0W2amQ6VV4uqc2KyHNLYpSmztFxfWJAWKfSqXleUahPvawQ2lWtSDBwielwW3xnR8QoyeGHM4xNaQ8_eA59fyIpSeQrMynRV22mX6kx2NFr5P4pXn3muvpVigRV8ySYK9rwgXx8L7s84oA_RSUN1mvwDitwCJJc5vDqT0CG78JyKykdXel9PwUBnXnei4HslmSqvQaLpd5ZRiSwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=QXYvXi9gOs08KWzpY5hifYmkHmdX19VGvvo8MM9Bz85GGG1MsNcC5dgTT-rtt8k-ye34b2TZYb-U8OvKUUD82qd2s_dLTTbn4Zas1paQrJVxxQGc3cpa_d3a2w9yatyWjOnLvo0W2amQ6VV4uqc2KyHNLYpSmztFxfWJAWKfSqXleUahPvawQ2lWtSDBwielwW3xnR8QoyeGHM4xNaQ8_eA59fyIpSeQrMynRV22mX6kx2NFr5P4pXn3muvpVigRV8ySYK9rwgXx8L7s84oA_RSUN1mvwDitwCJJc5vDqT0CG78JyKykdXel9PwUBnXnei4HslmSqvQaLpd5ZRiSwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKUmrLj0Gia2kfyF3QnMXDoHS-x42qExuGcMYTNqzsw8AHtF6xjioovQM2JSrVkijSumWYlCqybzp0B5_6clAbXUWPguI1-jqeqJRVwyDDi9PQhcxoG3igvaIC-XI5hvfMmdD7Z_Dk-zaz6owltyeYzxysA4nbU28eQMdo4Bnvua8HB909ctDOY1Qy34GMr5Q7dcY-R-HcsvoYI2TWNihpyv8M36qpyMvE3Lww-0jIJEdzvm7yVHPHdXcDmx3Wsc-6PWfSaVDD_7IZnXix-7-lUw3xogncw-COXR3Gh-6Re_94c6niMFCF3kqt74FuHtt7RHCXoa8uC6NhplTuTQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=JB8q3xtvwA_t7-ebzWt9-rQpb3peOqPihs6yi1dxG6JE6q3TxYpftPDJhLWSGs8lK9gMu2Hz1ewsvHp7O3w9BVf2gbU96TTgXoAtI0g11HrEQg8s6Kzwtk8hJPj8xaNl6T3RpJ40SSOF1UnJnEyfDtLOiTcOTFySME9C4vS8pAx0EArQxTwMFGbOYh0LI9uizG4H7WFSavLRzpXruAPcPGp-5c1wqRWJfQJm9dxgdMJOy--8Q-bapK6xDcd4F2gkxUddRhl_E-oFXmUK5fX8pb0zieJ22HjbqHEZVOhk-nQOBkIb5SSqZj8kxvKC34WFx4rhrSQPqtIvJwJRZDNJRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=JB8q3xtvwA_t7-ebzWt9-rQpb3peOqPihs6yi1dxG6JE6q3TxYpftPDJhLWSGs8lK9gMu2Hz1ewsvHp7O3w9BVf2gbU96TTgXoAtI0g11HrEQg8s6Kzwtk8hJPj8xaNl6T3RpJ40SSOF1UnJnEyfDtLOiTcOTFySME9C4vS8pAx0EArQxTwMFGbOYh0LI9uizG4H7WFSavLRzpXruAPcPGp-5c1wqRWJfQJm9dxgdMJOy--8Q-bapK6xDcd4F2gkxUddRhl_E-oFXmUK5fX8pb0zieJ22HjbqHEZVOhk-nQOBkIb5SSqZj8kxvKC34WFx4rhrSQPqtIvJwJRZDNJRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=q8pL0DWhjia-KzHp70Huy5cRNMWpxrFjJ3s5gNC2DxmuqDbA28SsIEtcG_4UxFhALARpfbhHlBByX8-aSVVvyIL0IdJg8gGXsxBJi2ih0DpxoJ1HFjiaAtBidc1WDw0OoguHSCFbUCrDOOVB-D_tNFt5McAGh6ysW64BzOu8SAMo9wJZbGTSUst-pQqouIRWZbnQo5HUYv82zZPXvNHsT86PC21O3c_vFxOnt9KtYYlI35_-q_wHcjtHOLB9mQQPHV30LFPdBtjFUO_3iUk-uBny_iVuKw07OZRKGBUIn4MQLq2qBFqUzZwRwzPgoBSbLEUVLTDWTnTPIAhmVlo7CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=q8pL0DWhjia-KzHp70Huy5cRNMWpxrFjJ3s5gNC2DxmuqDbA28SsIEtcG_4UxFhALARpfbhHlBByX8-aSVVvyIL0IdJg8gGXsxBJi2ih0DpxoJ1HFjiaAtBidc1WDw0OoguHSCFbUCrDOOVB-D_tNFt5McAGh6ysW64BzOu8SAMo9wJZbGTSUst-pQqouIRWZbnQo5HUYv82zZPXvNHsT86PC21O3c_vFxOnt9KtYYlI35_-q_wHcjtHOLB9mQQPHV30LFPdBtjFUO_3iUk-uBny_iVuKw07OZRKGBUIn4MQLq2qBFqUzZwRwzPgoBSbLEUVLTDWTnTPIAhmVlo7CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1WYeCCcj_R29o90G2srWV0xlS-qo3rmDUuDGBH52fWP3jbb4kWkxVKi5phzDKOysxTf54J2HLibUV5IbYhzDtWzJg7GZjuNUahbXi_WZcPMqauWglYKodDuUch0LceDS6ZK6k4r38rWiTDwj2_ExsqELdkj8632ycD7PztRc7LrJpsU9P0MlYc9hPcnsbeWfL7-6jQNU5h_GBE5FgHTXLQ_ppdfHMA29RyExY2tkCIE84b3n_Xll1809bmJZrEw5ZfT7RflKs3qmekMrt5HgWFt01VQ24gprYXLwIJp1f9MX_eBMmHR3lEcMI96yT2f6SJxkvjgSCE5-ZfpxozHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teYphgNA6NY0uQNecpn4X3GYneubkB3d_6IcxmAmKOUZljZOxPQDJ_Ox_4TKidbAotop0w2-USXgtbYGClypC8KPm4iWeCuBUMzOlGge0vl1CXandiBec5FzQ_dcwPGrLCXxXVcf2a1Bizi5yuXv0CkmRokf60tf49VQLT9mTghVneReIf_KjUwq2gjR1PZ4ksq6-rq6Fz9zl0SfDwXvSCwVBUaykSPD0sVb8B8awrJzyuGmI6Ub3te6K9odkTM_FY2w1jUpG_svm4dfnMtHshFxnMK39typSatLkNQc1y4NQzdwH5wHd6gm9kCwjL9RFLstZJurlErBx1YxDMVD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSs_84UgeHf4UoFENAS7krjf7EERkroKNPBnZOrZsXMxDeqpqltS4lrA0sKlNqrOTJXw3AiGXrUto_8wfpA1ayz2c_AaQe78XQHZ8XSf6tsz0KPWiIi3IbJeVjNmF3uDdWfM_L-v_UW5fb0FV61R4Tan6cKMvcJY1O1pTZnYQ5rQ0AVSETnNd-KjRSEabKJ-2Fw282Jbft_woteM6zetfju8OARXPKTyxvmFThtuoxmwaUNTDlggV_wXze2COGI5a5UN-QjaucpSTgOHwQXudibw1QLFVIFtvKTFAojPgiCmOf24Lv_2PwtVI7synXeDxN2Kdu5RIJSbUBvIP4kQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0gOvVqbJ7FJY5XifyFQPfcPvZVYKTajsaMDEcyFsu8L_w1ppTFrkW2OBGsmFwpAptO9ep0S7BHODPvmlvcdVOQK3AP6-tzJD9SFFEjczBRXtKRY6BEwargsb2wy9OHmWSVHYN8BtMAS0dMsSlZE-rJopeZb8xrKZ0w610wnZuZTdqsedaDEw5BWY3JtnRvWAY2PvetVRPLt9dzfB6DLNfsg0eQ85NzHFu9LrKwrcQomK6UatEbsB-QfxQfVYaG9BM3NCTZppE3Kb15aCYqCzn8WmD1-s7vzltfHKFQpAWYud0CWZtB551FK6Tu2mv0SHAesvUfFagsA0sNm9p4GsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVpWRNvdzW40Iw1mvymEtGNBfq9_uv23ie2WSnytRQdRRDB-WS4Zliz22_iHX5nwN7I0CLmiL73NesNFWa4s4pljwjzqqoMwvyXgbRxx1MXmVKdJC9dKCX3_O0RNWHeAbZ2BdwkdBXepvE2dJKFpLxO8vQKhZYKG5d6MwgCSFgm9Ci6jfJ-cA9KJIcue8P1hw_DWx2Ikyu6CZLikBftQ3CXEjODd8M8xONuE5bi_FAGDpddxH5ormZYO-1rejvE8D5qiV7l4DnIOnzR1UWLDBKC_N_myxyKeg420AUcbxY_ufapTcz7IWx9C1pomhM7Zu8tIhVpfIKeJhskHQji5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/petzrdAjhh0Qols8iXrs98BtyVtI1CdvZfC-PnhAeUAflILaiR1CB1Y9AmkwJSJT_l2G6ykQI5YgNcYY5Bc33pKrDE2uXz7f-g7l0VaMZhoArJb_j0RR9J6uVPd8nLR4SZ4fUq8IBeXCETld2CcoCnO5O2ZdkIngDSQIACbex7hVW_Ju-pTVFyNu44nqNFmXCOb7R5xG1nbFfHa-Thud70Aad416CEfd7v98nutXyGtiYzI13fj_liO2e_KjjU_8G8E0yPgRt-jGihVJAsvZR72e0r4zcFsdIFHZdhCW14V8XgIFhu_Jpnwkaym6qeeUf2uNU8bnG46cjM-RlUOr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmVBt1yDWwZ0VuxoidFOwDaDIi_sQIY_Q0a5MlN2iyBw2PkRmbnFJJuEgr98XV1-Spu0_ysV0LBjU2UvQJt4nwrcKh6-Lzp1PoEeAk11jazr5fcUDxFkqwlseWahXRt5nbUxMDiHh2xMkm5oXybFiH1zbMz8ZvJOc0jx_V4DFjgLYeY5NjDYQngFA_PJ-wXYLPQgD8Z7WayON4gjsYyPgD2nY1uaD0kGBhGso6QiJ8W7RYEx81tHeFfSEWIUSSTOLMUo8K1BKO-fnqqgKjIiFaqoyL2MlIUu2hVWhavB2ailC6PcxnzL1wf4SCG0jNlENmwW0qc2m6m75wDIHe5yDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8eX2vjrLLLWf0moZSv0a3GSppoE8lWKakLr7hNSrD-6hju2VLBUjgb1lX1s1bDWswXerDZtRSmcYbhJedD0hS5ScQq5Z9vHsIsL-31EHAA3Veimxld62QUoxS6ZlWeY0JJtwQ0klPUCH1vgxWKDm0evRXCfSGnYoj0QGXXBy-Tj8pNFwBRFhWdE4apCV8pzOFeK0XeUEuYNiHcAyLEvC0kdaoDilTrU-Uk93bQ6gVNb-S-iqiDBBpfMm6gaIZs0CZGuSgKMybor150_avBiqeN_x0plDO7dgmKxMN2UH1Soh6b-BjkTr2eQ-kjMxMM2FJ8rlteF7fQVAFNbi-awCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IibOisP7R6rZemCh_VPQAp78pUZYgojK09h4wWY4xRNycdM5M9D3PVEfg4EXRk-6-a6uADn7a9zifn7LYo_ls0MiJS19zMlROr-Kr07mq0xscaFllJbYWqF1ahUKzme_JBAUZW7bJ347v0WRZgP1FCsQfenysonJ73uNwMt4aUK6yPRrXzm_VTS5HwKVSJxqGCTKcObl1hRCf68B7wdFqfvM0xCMIhWh-fYtzheLrW3Rv61OwQ0CVPvUDuZJ30ZiYrsbpq862BbzKzXCehKBxD17yFJLw7W9RZREz7BQlhbBeI6hy_eQbvKR_K1nBM3DprA2GGOF1dDkzz2UR-TwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-KTsVJYfG_X5_79LOKpVVwxPzVTFTWgblK8AVPJzJ4yJobScttQ2ynUKkw1URqfsSQYy93Ke9aIkEYcrqEbViOyYus-jKKp__gIWSM0tj1ysEGRE5q-0rk88_ivSkUd1cQet5GQP8zMa4oPMmMfWAM_4GjziCUYPr1kDhcfuQn9Rl5PU7QCEUL54iS5GMws-m3iyZnl5I-B6k7e2WBVWwKfAhgYzjm5YuAAa4AWr6JYaNz-h3gVfbVCcCtPfB_W1FgyWFDTcasUByc2eCWvl_7Q48rjWYxVfN7qCQ_El-0oB2UNl5AqKXEZW2Gurw-dwS8k53eEa5bxYnzR2DhfPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=RV-95MZDXMfP5c9PBo0oIZD99UCaRv380xsfRtsXqwnBqBlW4kJhDoL7Gr93x3_JanKnqlZc_IZr2fuXjgSUPJ5oAEABFbxnJN8u49iPTSASG7QL5qpke1qYOv9NCjYVprqe3QzCowXdUlJB62mCK7VXNSFjUal5u2Tky68PNFoCx89OzxUOQY36_vLtkqr5r82J_LCN1aAATHashrfYVfwVTHvdAkZOJnfdTmMpM3pCcizO99iPQYuYcmhns4yZmlI4wY0BNCfdpyyMBHheCt3EbSeyeGclkvzrjPW1CNtn4iRQ0apD-tNpwLx7rOVsRArLp4IsAjyYjIX8GjbM5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=RV-95MZDXMfP5c9PBo0oIZD99UCaRv380xsfRtsXqwnBqBlW4kJhDoL7Gr93x3_JanKnqlZc_IZr2fuXjgSUPJ5oAEABFbxnJN8u49iPTSASG7QL5qpke1qYOv9NCjYVprqe3QzCowXdUlJB62mCK7VXNSFjUal5u2Tky68PNFoCx89OzxUOQY36_vLtkqr5r82J_LCN1aAATHashrfYVfwVTHvdAkZOJnfdTmMpM3pCcizO99iPQYuYcmhns4yZmlI4wY0BNCfdpyyMBHheCt3EbSeyeGclkvzrjPW1CNtn4iRQ0apD-tNpwLx7rOVsRArLp4IsAjyYjIX8GjbM5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNbzvuwy9L8xfuImNrJDu0qIroIeUPbXh8XBs7Z5AgZr6ljBxTHvfUB9NHco_SfLT_DZeXIThEvZ8M84zS6ELXpQ07s2QA18QS1U9cxA_nch_sogKAHS_gxc0WOpHRrOUk90S2lAi2VIzBFHZQKs798aTk5Mq0hY7Ur26nSMrML9CgF_hzM8Mz82UzBnc5ladvH6pecxU1WqRL-7Idw-XbuWcQcZL515LjmmJS3N-Ru_lAdG4KlbmKLppz5J1OIAqPLM-b2uyduzVFBY6SEJLY39UAZyGOeJuQC591EOIT-P46Hfix33-OIna4Mo9vyDajBsn4-gpOxhfU7mIu4DEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs9LUO6zs_dkMhDlyJyDb3DzjndMBYnpQvv4s4lAoqBStfeP7BEag1b0adFLykuC5OUBcuXcN0ocQFCxw2mGKM0tcSNspK6fnsHVOUP_PWV_GyPTs3yLT5O9oKPsk6HRZWWP3XQqEvuMxSSmhnFbx9NbeMup3CXTiJCCC9qWAbd7oUWlTfAB2Fb_HJ68vudlg6bnUimHwUZphDZo9-2D4zH4TUB_RPr8sdIiGwtdeKKHRjKsNOJSL3-RuoaRIw96MSa65QyX7p4eiBl24FiKajEzJ5vbpUg0RQkCjyuFOubi8Uc6vJVsJoZS3Hx__oNBpX43qowteX9CQ8wGX7VvjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=ZYmdbevj53kvrEeLmBXAY6SU9_FrcQ2g3Wvpn6_HjlvBF-sy9lFJjt2Qv5oMMnMO_VXTu24C08GX_lOKioi5uXrSExeGC9-tbAI9ccRnI2PZyqe0QJPlxEgIPcrOc80rSxYmR-E4X6UAvCZcJ5K8Bb7KlfiSJ-y946h-XNj6CQKKiruLNbfTvOUFTzdKQbfXCp26y5-Y2Pb9Co1kYG2zHHba1f-ryTFz3njCByPC2PzU1D4Hicy9q_ezvyh2Tc_pfvaLAsvuBbCT_omgtWhrBJYh_UcFoJJhVcFdaPu7ie8LmQcQx-H246P54bntmbCVzBSrZ0Kgtf2-KRkhMmMxVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=ZYmdbevj53kvrEeLmBXAY6SU9_FrcQ2g3Wvpn6_HjlvBF-sy9lFJjt2Qv5oMMnMO_VXTu24C08GX_lOKioi5uXrSExeGC9-tbAI9ccRnI2PZyqe0QJPlxEgIPcrOc80rSxYmR-E4X6UAvCZcJ5K8Bb7KlfiSJ-y946h-XNj6CQKKiruLNbfTvOUFTzdKQbfXCp26y5-Y2Pb9Co1kYG2zHHba1f-ryTFz3njCByPC2PzU1D4Hicy9q_ezvyh2Tc_pfvaLAsvuBbCT_omgtWhrBJYh_UcFoJJhVcFdaPu7ie8LmQcQx-H246P54bntmbCVzBSrZ0Kgtf2-KRkhMmMxVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=eF9XRu96EyScnLGOOe_SQyMl5crUbdSgwt9KRLEZlKfxTZaWDPB15LdluOPhoP2NsQM4YKQbrtw2oSbpg8H-ShIWAY6rlg_j0nrvpS_LPWC87xAo61cyRan_90eOYbpFfIt6bBr6QVlf7UK3qSuJ6icUK4APO00jSg7OjzVx7WFGk2PKfD5hARRUqyg7wCD1SoA-mm4pPvtvXTqtWaSnMVR_EQYyVwA7efxZa0kDUuY8_AYdQLSCcoy45kSy1fxY3bZaPCreN59ciZHRSsYm9WWGwbs9UFcYmLKeQqNHCntEeR6R7TWF7a_V9xet4v_951aMhjn6pcxyeuWYpc5r4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=eF9XRu96EyScnLGOOe_SQyMl5crUbdSgwt9KRLEZlKfxTZaWDPB15LdluOPhoP2NsQM4YKQbrtw2oSbpg8H-ShIWAY6rlg_j0nrvpS_LPWC87xAo61cyRan_90eOYbpFfIt6bBr6QVlf7UK3qSuJ6icUK4APO00jSg7OjzVx7WFGk2PKfD5hARRUqyg7wCD1SoA-mm4pPvtvXTqtWaSnMVR_EQYyVwA7efxZa0kDUuY8_AYdQLSCcoy45kSy1fxY3bZaPCreN59ciZHRSsYm9WWGwbs9UFcYmLKeQqNHCntEeR6R7TWF7a_V9xet4v_951aMhjn6pcxyeuWYpc5r4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmvnI-XmbeI0t0zu6XYrzd6P3PT4VUyzcCxFKzHJldkQAFJNrRhjuLTg4nA6_ulrSXtOS2V8DijbmtVT2auamGaoyGAzAqGZdPTrSm3i2eU8E5FQdZaqbmUh-9ngx1CpLSF_IROwnwsfdoTTbj-EwO8GCuC2UEWUHiRIFeIWVUXQHbDVxoSWqSFFyDYNTjcyvDVXkjPQdH7EhDGRDCAAmpUVGCb7oAlX9sfmnTPCIprb8cqlY_crwgEIhw4qtGYwnHwvVVtqTc3WmsfOVdE5y6Fj74l-KwbvlHqXh5Px7XEo7QlNASAEvOap5rKrPCG-I9ZfNlZ97H3yGUv0C-OK-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRlhEQ-P7cNFmEW8JpnFdM55Mihv6fKyCJbn5ANjWjqwJ9YK3allbgGMK6uM2UlTK5v-bS2a_Pt8NNubAC_BJV1tMECTO2cx_4Cn6Mr2YwxYLQjQOfm7Ib4C74-4ZmcsUZnJNa7QagnfFy5xTiqQaO5gTGcfHMjBOV4Bx8EXQEnBa_PeQ4xgmPrDzDYOOr-KoYpkLeJN2tKbnITi3DJv8W8EJep_eC3e1Y0Ee2zdVc1UCT9A1xSMjbUhYXikzPe0dQTR_QaRifin1vSqgj08XgMXPT9KGUiTOT-atORBF3zsl6-fVU0SHUHqD4lSWP1MpWnxHPv3Cw34MAFKfGIcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcyBq7Q-2isgqSifDDrtpotjtE_e-U-Bpo0f0Kfjv6TLtfbYmjd_m0X7d5Yr4JCWIFckIIWGDq_H08rmzlHWO6Hr_y1hYnx0TuD7liZcsmJhKAHVTCMLotffWxqta2ALN8UXrx44oMOGaU5vAsWthOkTywbKER6WIOqdGdoS80zmsQlrXMDK4RZbb1OUYNOao66rStmuHQQmpmNlY8XND-Bviicg7f3YSKShY2IRH_OqB0daejk1IPnFN2PIGuoPnDdXdgU9CDNFaV_y3MvVnlmxuw6b0KvqQ04zJD66ugUF1mk9lxvvxy4yQiQDhGHWoapMDiEFnWy_GQXcNfw1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR-tsiwIMXVooCg_9sQN_VVTVLZwAHQiQBTvg5MtIOg7jnyADUj94LBwwhAl5TwhDg_RsSmPC8bZNyMkcMgALIBrfWnl4RoEJR2YVYhDAltrn4AUPazBomnmWp1MBP8nJNbh7v6lsdYKmsbWQon2vp-3jVD01lvZJHl7OnfMxBbwkZIK-tnV-BEVfRGcEiQWL4SWzN8c_i-HxDA8DdjMsYpEeluNpO1v-HPT4SaM9KpuzbpKRE8nXMqfqTsOJeZni7q5zfq1LxLJin7E30Rzqg2_lC0artMVll0vkmelw47I3L5bfDWIaQgevcH90HfHVQm96qfRa47mxr1m4QQQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQfFtIqAD01wtqEAoWUbgytcdDnrGJnCLIHbqiPJ1WfFPFD0kaBpLeBqGYNNNg_bzx8EECaumdSEbpJaxxIYvaJ-aNwHUTtOA8LzvlUwPC-esEGxtZEOmxr6UgQKClN2ycpySrhx_mESkBRGJKbnvH3oM-KKIXM4Fwvly_vWf77VX8fBzd4LjgQONQyy5uSezzhjMuVmdLPYkLkvl1IQzHjrW7W6OS6k3r8U93GuFoQ_wfb_Svg2VRbe90r1erl1AJT4qy7eXtK4YDaizqCd7UsmcOZAaKYghlT6KRo2IxZMwFF3k5FYw9t1821PkMOYThLu_G8hmuQch9w5lpIz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugsgoWnK2WI32PSA7aouiZb6exY2-uPzWc69lvM_icxBGFtHml9bbVOQABt5o0-fplWCjghnj61_4x_W5RAmkNrYzNrUdgD12Mc8ZL3sFBfnRx9mqhRWrMM3Zu1tiY4PjJO7POp_zrKnoG7ZnpK23mckXdaRX-glo8UNXLBWWMb5FLINp044tPQLyagU0i_9JMO6cxsZCBov1aCmsPMGr3uaGHZM8tPxfuxDvnaYLdYeaR7WplidwI_i2pp8IuA_cmSOxT7iVMWh6wuGRB_Qo8VabfhL3oO5KhxQo9q0R8FBXAk39ZgYPsi2HvmAwHqzD5WLOcny05qKlBPmbFW45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGwq-xLUAcva1r15LHwPdWeKp1igoBNasnyUgA1z6bwpCBkFZapYFazVizLv0ZLanArIAWfiDuAw4o9E9znvDOQYxteFryR_9juFe0qIbGKYlEVUgLUd0Wxai4DR0D0MwcP6eG98Na3uby9l6S1Cf7R85SA2CM6gMgNFrD2rQQvTmwecbFfR20TgBNcSvdhk12Y_SM9YNWMHnH9R_pTQCX7nO0b_NAmouhjgGQZoWRYP1AeEc3-gpfpNkjz5YGrjuOCAbpNFHvbw18gJ8PD4TxJUbwUxAZs-BHBI776Wk1vl0CPVwyGJhprgPdf4YQGXcXPELd3ujCGSTdcxUtkCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnskH5YdBBXrksSaiQ_1U-D4CF9dc6mplbSPc7SkYgYsiYvAoIwGVcMQOmGS5NuE7pxp95VHgaoRHzeuLNMld3gnZSr344pHfAVqNXihdzb5R7J85J7NK_ee7rw0lwajH9CGv_2szj-4C-HyTT65PJIULtCJQSz7d3HMg6dzgehuXG0IU1bxVbcVZ4qT-uh7ykF1gqNDXGyBMeOkpACxxVkMAOYyV8j5rnTaIG7Ady2I2qGGnoVlcN3idOMD-pi4cEMFa4Mu6ul-PKf-_Om6qIMA0RkUa0FEX7goXVnoMfqVP0weTUJy9Nzx7_8cTuTWjzlqLUErPRRlhyq5Tk6LlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Ct7DVJm6MzfjosifRHjPtG7_v9nIAi3GedkXobAyRlki0dtS-zZQgsJpnYCuruCpEdk4fyIyDRX4r17kFX3WeoTDKg43j5IeNvCvSZsiscy1wixu6QVjLmobKoXgXMC_-dhE5CumeYCKztv_IaCrZz4NnvB-FmfZt8gQX8a1W5IHspb9YCZicaBd4ONrLRT0cKJ4DhjiCV0xbOxlozfbN7AfF0U60PXxXYwvVgpCDr_5uw9sd0c8VIHLNCXCdzuJIYIVx24r96fov2I0iphMnDIpiY-VOdF12ChVyk606WpntHoGkM215fXmmpa5jtmrJbOdXa_JZwWFBRAzqx8YaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Ct7DVJm6MzfjosifRHjPtG7_v9nIAi3GedkXobAyRlki0dtS-zZQgsJpnYCuruCpEdk4fyIyDRX4r17kFX3WeoTDKg43j5IeNvCvSZsiscy1wixu6QVjLmobKoXgXMC_-dhE5CumeYCKztv_IaCrZz4NnvB-FmfZt8gQX8a1W5IHspb9YCZicaBd4ONrLRT0cKJ4DhjiCV0xbOxlozfbN7AfF0U60PXxXYwvVgpCDr_5uw9sd0c8VIHLNCXCdzuJIYIVx24r96fov2I0iphMnDIpiY-VOdF12ChVyk606WpntHoGkM215fXmmpa5jtmrJbOdXa_JZwWFBRAzqx8YaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PifWGzCnp3LQsfO92iphhN6mfUCCIiiPz4hz9s2ul5so3rXTnXeChLm3_zUnZFfhL8UqPz5dYj_8NpMNKs725i_nJpR26P0JGbwM7_WTXWnOVYDoxFRCWdnyGxr7ztPs66a-0Iw5RiJvIB2Ycl9B5ajYguma8fs8CIZppsb7GHLJLcYKQ5Ggt-Aoe_JDVntA3dNHaHb8h0WKXxKebZRC_SpH7FKtAU8_Cla5niAKV-bMZVMxpnBWjTnTPWkBsrqBH4z-ufqghP5qJQPV56ZDNh-A4F58yE8llLdVISCOFeHU7KlKG5dyH6uRyZiVKD3vYiWtfVGap51eVlRAhzJEBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=mv_IWIYGYimVgwcYOfWY-XkXqpU86zBqkCEIOMY2uK5aFzRZOpG2Z5ppZbp7xpB1j__-kaqTsOhEyfJ6SUNzXMr8e00XAt0pmq5wWY8ZqRoWkLsmxuh5V5PDezJCy-Oje9vTLKXLbmbSU6t2C6gjckfPEZ9oEOLVHGzrI9BchCnIQYj01MTzlXqhrPLOAgYS7P2gatTuG--fkHwGsXP6_5oUEIgNuSnYfNCux-gZAm3pSR98mcN6N7Bu7jNyZ-hM8sY84ZfCPrK-5XHQ6uU4sc2CrbCGXxuFt0-1rMfAjNiQK9Xx4iass1K7ycRQ8saH1u2t1vguzujMQ2EZDjWTKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=mv_IWIYGYimVgwcYOfWY-XkXqpU86zBqkCEIOMY2uK5aFzRZOpG2Z5ppZbp7xpB1j__-kaqTsOhEyfJ6SUNzXMr8e00XAt0pmq5wWY8ZqRoWkLsmxuh5V5PDezJCy-Oje9vTLKXLbmbSU6t2C6gjckfPEZ9oEOLVHGzrI9BchCnIQYj01MTzlXqhrPLOAgYS7P2gatTuG--fkHwGsXP6_5oUEIgNuSnYfNCux-gZAm3pSR98mcN6N7Bu7jNyZ-hM8sY84ZfCPrK-5XHQ6uU4sc2CrbCGXxuFt0-1rMfAjNiQK9Xx4iass1K7ycRQ8saH1u2t1vguzujMQ2EZDjWTKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=ceLWY7MMqIxF3Xn_tcvB8ZGBf6p3lYy7vQbYFFORldtB4sSpOAcBiim2TqHE55FufKanX7G6Qvk-rGLAyM8K0DekIhGZfr6476qKD_F523a7ymdmRNOzEBcZes1FE8R8u2PKShbrtCQWASMX1rCLX6vQ0SpLHcK-y9b4wHQkGbxidxGekMgPgX0GXHaYTeC17s8EHQeqboXF3lg4siXJZ9vAgx0UiePy2Tg1Twxu6BoCx2PLUlXUApbKwVa-hchtMgNUDnVRJycpjwLQTlJDd3Xu5A19GBnlex9xsbroWRk4E7p-4sfN46AuxUuDw85s5Bh7ipEkMouAYgAe2qBGfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=ceLWY7MMqIxF3Xn_tcvB8ZGBf6p3lYy7vQbYFFORldtB4sSpOAcBiim2TqHE55FufKanX7G6Qvk-rGLAyM8K0DekIhGZfr6476qKD_F523a7ymdmRNOzEBcZes1FE8R8u2PKShbrtCQWASMX1rCLX6vQ0SpLHcK-y9b4wHQkGbxidxGekMgPgX0GXHaYTeC17s8EHQeqboXF3lg4siXJZ9vAgx0UiePy2Tg1Twxu6BoCx2PLUlXUApbKwVa-hchtMgNUDnVRJycpjwLQTlJDd3Xu5A19GBnlex9xsbroWRk4E7p-4sfN46AuxUuDw85s5Bh7ipEkMouAYgAe2qBGfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH9hv1QCd-_K-YuRsAYMXLiEDYZzOQGz3rMetyGOOIXZxwhneliL9SDB0K2JpqndcuPB3hzGpF8Midl8oGgZWmuZyts6HlsOQlXmdf4mP3eEOVqroNyEkfqQI5mKN9RSddPRZ1ft2gCfRpYAe9rnEnHOX2pwPPbb8qHYIstYodJZ7K0h_9z49FTflK1JtRW6D8Khcg0DIYXa1xDZlgz4ds2qq2S9RLpPYSgb5NOv8EGEWoHKnae-yRIBKosEE7hGXLpclSl6DYhuxJ3un82rOeP4XLDm_Ntt79qQLMvYPz9QJsabf0X3n-i1KGoxTW0VuSVjVOdRIkG-A3g_BEJ1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkSZO3LwrLBQrkt0z6OIIzR_0j9zOKfKSfRF_MjqqwJOvPlOYmKaPtrUmWbs1gN2GXC0cnvdOdHPPmOkkcppS7hsd816NkwT6sELOJDchbI2Ou7kk1fP92g45BsHoVmO7j0Wce2geFV9lt1ehBQMkK8cMae53SUZYqvuvduIQeEpKMSbWY_6Ww4_C5JgyhJbPrL-OQhD9D8opG7SQt4OLgEzhpbB_Nnhhmh2MBE_BzY6391FkruZwsmxviOSJq8I1aO2-Lj0RETsZrhGfiog68FSJ1qm7bGfIDJxN78H8RErWY4XcuymReJn085ElyQQ2QsWqVSH4FDfGXyNEOkHSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=VMS-Lti2lH3XjCNZP38NQkCp8EDTeVMe8afTghajDinKJbZkJotcYoXMce6X5FSP4xD-waRtY0MknrGX_Gv-TL2534k95BuxOiSzPTnbEPsSiY9oytfyPExM724bwCn1QrQp1HNGvS6JJ0J9WF4Jjw_iowomvQvE9cz2-2AA1duekgZVTuqaM_69FZkEYGgWvMVo2H-buk3SbUbiQzIKeGXgt7MN4FLiygaootQx7plLAu5xer-PfqC0H0jIL8FSCyVUzVInAy3wK1a2q9fpI2aRMrRFJ_qdyzG7LuaU_5HTka2aihNkM3PgHeUGdPScIefjz1qVwwsMB84P2dubqLXlh_AEmQDCwG3YeWVNxZpV16QKPsE6RYPgdksdQZlaCpqvTRPzZTb7-ZMtaz96mZHX8Qm1T75W8dteEZJlZc2eDa0PeJsGv4IP2X8BTcWSHB3GXzJ01_F-Y_7aRP-iusPBZ4j39dBpuNngSPu1OzPT9HG6O_ag_Ikd2qRvdw9tuEhFXQsJl5TaeZPZk_dRDPtQkxLPn6SHyqifjIkchP9tu9kvP37bcqbA2HLbKR9XK0Gcub96rEb-_9qb3fZ4M13Ab5QqXLVQjNU5nb7_soe_R_DDKqFE3U3J76-K6lPIMQlFFU2zoJ4cJqcaP33xAIiPX-J9plpabm6m886Z7OY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=VMS-Lti2lH3XjCNZP38NQkCp8EDTeVMe8afTghajDinKJbZkJotcYoXMce6X5FSP4xD-waRtY0MknrGX_Gv-TL2534k95BuxOiSzPTnbEPsSiY9oytfyPExM724bwCn1QrQp1HNGvS6JJ0J9WF4Jjw_iowomvQvE9cz2-2AA1duekgZVTuqaM_69FZkEYGgWvMVo2H-buk3SbUbiQzIKeGXgt7MN4FLiygaootQx7plLAu5xer-PfqC0H0jIL8FSCyVUzVInAy3wK1a2q9fpI2aRMrRFJ_qdyzG7LuaU_5HTka2aihNkM3PgHeUGdPScIefjz1qVwwsMB84P2dubqLXlh_AEmQDCwG3YeWVNxZpV16QKPsE6RYPgdksdQZlaCpqvTRPzZTb7-ZMtaz96mZHX8Qm1T75W8dteEZJlZc2eDa0PeJsGv4IP2X8BTcWSHB3GXzJ01_F-Y_7aRP-iusPBZ4j39dBpuNngSPu1OzPT9HG6O_ag_Ikd2qRvdw9tuEhFXQsJl5TaeZPZk_dRDPtQkxLPn6SHyqifjIkchP9tu9kvP37bcqbA2HLbKR9XK0Gcub96rEb-_9qb3fZ4M13Ab5QqXLVQjNU5nb7_soe_R_DDKqFE3U3J76-K6lPIMQlFFU2zoJ4cJqcaP33xAIiPX-J9plpabm6m886Z7OY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvFGuVp0WMy7Ud2bggf9I97h0DJxtj2dTBuJ7pbIY57HMEw7uJUlEpLx3B67YfPRe1mFmRqhjERd60AbUr3FRJnRqPZ0-L-MAKcHlrEC-PsMngUHqUs8dZq5JRv-umnnZ41EJEMZ4COg7cNuPg4507T7foMohcgSiXGVEqfoBYAL-3MtJWlii1_sY8kJaCz2QV7Pzpm_H5lovkt4FyzpRU8x-2FegkNThYWz61mvcMmuD8O1kDt7AnnOo0gmFH0SMmfTih2XI-p7iQb4-exZWKTZxxDYHUg-5IgyxV8YIZ6C2pNPYKuPWjSPDo_xzfDxlEgOEekKvFgIepokc_9t4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=D31JoLp3zcVioik-oCqXyFPq6mwl7_SKlJfaYfnAG2tA_83r9pxfxZh60kqS0nM9Nnzqzj0DHah3R0njqlKci379Ee4oeB2jzH60-E-FbRlh7wvVs0W2yITzUANJc0EfPzDOy60Am1l-iyoKq7_ndYim5u7kQ8Ig_i39ucd_O-Q74erYeQZExOeK9sEEAbxGmfQZCX_pgPu2mJd0PqAG85JTRwXVSeEfgCdouZk76IncDuqdD0B5yEwjNFfJKUY7btMfRFMgmamietIObXUkXCO8DJKy3O_AWQR9ZspeVdSvTOmrU3M8fpixRpoBXq6fNiGVtX7uN_nJ-bxlwZlWRWx0npRacp8csZAMTYr4yONkKU1_oTAuqHimDbJ8oBGD9x3Hd9CAB7E7sKsWhby72R_2162mDGGjtFXsNrEMwQcp_0kMeiuOm2-e4HFi2jIx3VewbGSY4Q5BCQMVfnTeHm5iEIdCRFFXdtx1a3htFiaYJ3K_X3M7dpzWw3fmHPwbFdJEEuMy03VK1yx7mmLh7HQtaKoXQK1dwS4AXng2gUx7HZf9AKOKUAR0Ibv_vle6lk8O8xnprYNrXx0rDzafOFS9UOCoNYFXexR60XfYNccSC4dycd9-EfaTuhLncGEz4phVcoj9-I4pHp4ZA9hIq5OiaOnmv9viwko6hnAPwh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=D31JoLp3zcVioik-oCqXyFPq6mwl7_SKlJfaYfnAG2tA_83r9pxfxZh60kqS0nM9Nnzqzj0DHah3R0njqlKci379Ee4oeB2jzH60-E-FbRlh7wvVs0W2yITzUANJc0EfPzDOy60Am1l-iyoKq7_ndYim5u7kQ8Ig_i39ucd_O-Q74erYeQZExOeK9sEEAbxGmfQZCX_pgPu2mJd0PqAG85JTRwXVSeEfgCdouZk76IncDuqdD0B5yEwjNFfJKUY7btMfRFMgmamietIObXUkXCO8DJKy3O_AWQR9ZspeVdSvTOmrU3M8fpixRpoBXq6fNiGVtX7uN_nJ-bxlwZlWRWx0npRacp8csZAMTYr4yONkKU1_oTAuqHimDbJ8oBGD9x3Hd9CAB7E7sKsWhby72R_2162mDGGjtFXsNrEMwQcp_0kMeiuOm2-e4HFi2jIx3VewbGSY4Q5BCQMVfnTeHm5iEIdCRFFXdtx1a3htFiaYJ3K_X3M7dpzWw3fmHPwbFdJEEuMy03VK1yx7mmLh7HQtaKoXQK1dwS4AXng2gUx7HZf9AKOKUAR0Ibv_vle6lk8O8xnprYNrXx0rDzafOFS9UOCoNYFXexR60XfYNccSC4dycd9-EfaTuhLncGEz4phVcoj9-I4pHp4ZA9hIq5OiaOnmv9viwko6hnAPwh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZeIaRL_4AexgaMrL0YmWZBKfU_HKSGKrA09qLA_J-vbdSmrJORksdYM8usVWLLkALyzg4vEHAaXDgehyGtVYvilkHN2uluEL24acVH1j0tBg1uu6Sd1cPsTzoRmZlOLqa71kbMMTkxwnkQ6YqGYXh2wtR4fIN9fLmFroKFL7do7h4GmJkzTDAzh_h6mvZvEclVeI2GzZnOzJlfEluLZPpBL_IYmuzOh0kxfZJ7Mrf1MtjVHM0e-BPw2sIllNBvDAEcBmXVk8GXvyNsNvIXZ_YEzTbhvZ1O-BrhSVzMAB5Jbfda29-ntfbuLXGDietu3qoeekQPdqxKCGfRU45MzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFb9XeioUUu0nPtJtUX6xfRnNRQr9-zq9xydSvCvfSfLTfZPL5uHUtDqqy9i1jGDVVZPu41A3ia4u0wKKdWhErkaHGTcAm-SYvmaCPCScr7SNcgn0TXkrCXBDdOG9pn_VsqJRMwHCMH4kbg6v501P5X2lQvS2acMAVC71lJyiDqCD8luCOIR2QNIX22r5m4UWKHkan3uN6jTxpqyI6gLDYUIHO9zRJyB1cSlAWddTOCNAEmmnHrzJBGF-_ddoOczXKK3si0J-xlW69lPDSZyo5JMotdU7NW_WLOfJPUQKS6PLL1I1iBuYi4gLXOI5IPIggQOe-uhVdOFS8V0YUDMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMj0mRUYaC67Js7x7ij1U7s4ZvNKElNUlNKHCSB7Ip5q4xvcwMqe6M0ddNVc-eVFTeZUpsUxvFcR-tcRJSxo9YKNFYrdpCwKaOoYupNUsXRLGyOG5vMyOhzK0freTtB4MGSm3yDKDhirh3zaEO8X9dJXk8pvqaDPmx9WpZy9hj7rxDCdoc6y29-JqXlcXBcLETGNQtDaxOEJDj20dz12kxL_P17P56sE1i6Lgp9_TFwu4BycPD0muSLG0r2f5Zxbit6T43GqZunaPQ1VjKIJCHaKXcbSKsvAHo48Wcl0MEgcTPopOsFrUInybI9a0wKAimzuZ2POqgbIi8sZnFOFXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX6t6gMZT7aEMk1cCa9B9B4Bvno1WUbn7p5HtZTza95aXB3bgT55X_bTo9oyzOineY1qTjvjCsU9dYvZDXcFHfeVWteZTEEuNI0zq4GbUWjBHgf6JAkQNOrGvyIbcdjC4M-hY4psy0xeTOtuf0EpcleQCzicYx7mbRzLJQ9XZ-omnH6Gv74yHF6EMkFpecznwucTwBVwJhwdEOZ04e6DIngDEKKA9-8G-K3r6b14diF5FQFmwHWgab4KYzgyq7SZvsVzVc5ng1tFfxeuqC2ZtFK9f8B_QEVHEHEGZSlmyuO1LuFPsfFox5hWSaGxGi3u10221slOf5gmzmzCS7w5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKdSjCrL0U8btEbpC-WBAZQ-wLxo_dATudxf1UBRp7dqCOMm1quVFC-dq9ttawsN8Li0jBQzxwHJ-WTaBfXnQAa-A4hD0amsuOd8iu2jkk94yYhqBox_8pLdgQJlq_Wj9qIHwz0mJKniNJVfjSVFOfbQPH5KNQ2un2yZv6VmvFQLA3OGB9Bdf02xxl63-oW2QSj3hHQRUvmz5dMF8-oYZyJZvi-ain4LxgsLIuR4s5NXph5JaJcJdKAqoB2zamOsnD3SLTJKRoO2aDjx1Pf2LY-MSL6YOWnFhJ-vZfGCLOuB-IxKpXqFzVo0MCpaUN3x8w0HzWoXK4hz9PJvrg5AIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY242hhATKhjP7NZFsGOOsq3kCg0Xy2JKC9YYHhkNh868R2nTekKylgbM-vK5ZzTWJnPagAWy5tdkzzHebrzoOoiW-bXFK9sqGta9Cj7a0E-QsVToR44z-8QY54YflHzwBOslIjyqF8LKnEt1gyMi8kOIb7XJz1PQSApQjS2NogW_lPxPoOJf7osIZ0SCilDYZx4Z_xLjg-J0_yhh0tF-3LS-otlJU-iJG-7zYKegWE0Xuf3Ol60XYs6Gl-lx5zoeSbQl78NqPseK-AEiLeKyBganhiFrzp5NILjLeNm2bOwdzMmYzsyrMaPCOydengzblaspvclEW5Gfdquzi0vbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcarEtk6TGl45MKmSu64l8vXYue4FhwPmALN3VSjWJsYbuGpsME5J4NncH-oU5eHfMTiUBt9nQvCwi8uWJT0Kh-3xFzXxh1cGpUg6py1fI7NJJlIYgiK-tjDp3tPueINvRDnyNNYXXVbg0A1EgW7cMlD8xdWzQnfH9euygGVHVS7rw_AkF2S81jjz-QY-yy7FSaW7ouNNEQn6AY8DVMEXvxfqiAZSnlZ-c3bQRjl6tJH3nWnfUS5SMnqCGWK_Hnc7b-WXOfS8GwQkOvumA-Da4__1l4RQFkSFcoxsrUvovCdzeN7sk8RBoUWANiJ97bkGAJnmNb09PTg4dK2Mf57OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feqqn27qmM7Xk2xBFWfwyRx4_upD8wSh3ChNFQbTFhNelRsFEDZN4vduuL6kysf3uU5wPO01D32ITATi7YAfcoeEmFlMBRHxSHB_eBIqIVZ7ibbpbB8ZLjdXbMtvhrmefpW27XWBjyczCUN8XUQKybMrcLMPUFuXExfhJm3VxoAU83ahN8r5w9iHWxqZSTRWfW-0VoaUR30KiyrcoljK_a8cHVGmqBueuiUwdGTiXA666AVCyxnvcr4p0J42ObwyRXDsjT4vl6-G4q5nlZOtHRMbT_jt_IOW76TVgjQY70CmFmox988pzlqqLztWH7GgyqKX_scofpWr5cEqpAW5Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYck7u811b7Uf1goCb8rwamt5PqeWuKVqeRdpoG5gA_q8Wui1U1jIa1LGewkdgXb6PUOyxGETkOVyNntxKBqSaUJKFJuvZRYG904PkH_m2SXuHX6SXqynZLneR4vwxVUw5iTMpEU8Zy1oGydIm2JP04yLgB926pTx_LPuZ0rAyTxpC2tViwTPSnrSoOQmPDJMvlCDlU3TJr2Wmeq4-kzpUpC8GyKylAHYvMzWErEJnF9czCRmj3R4JQRUswWnegDUm03B34TArKuxpqR6_XqZS_HYdvfDJCfBxvGMYbaEwUYIjsBs-s-NvV5xsXbDIRqnx-zgsfoP4q0mLmBRI2JGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORvYieqC4HvCvMvbMyO5GTbrJiFAeAMF91ByJqH8U4tNqkVvfgwJE_0QmW14swifcUXivN8GcrI-FQJKopiQzM7rP2qGs9zEGXO9VndHbnG64qKBBEFsf_QFH_tilhF6D3zxANFX0ZjGnfKEihTdcKaU_dLCN_gJgpCJDlJzakEk4KssdImBamBUdOXJzJ_vV67kTILduWryh1qJQg3GNbzu7WH6OB74jxKII1QbUB8vMO22ff0JfvyPwfa96mZ1zfDD68r5goIqG8ieKkdfI9hYRbhIyMTBZwnT8o093bc4sfPK2mCvDgZb-H-snR58lhCE3jl9QO_NgUtglOUqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5lE5hbLnSSwKqs29C3QZWt8_Lk-n_4HOVNwX96n4JRLO8oG0jvpot8GR-phDSaZu_OxyVUgL3e_F0eZ--et7-8WbwCuE9soGrL8uW0DxbjBEtch3ZrjkzRxd7ghB-HT61z4aE8OqWwLJPJzMDWM-IgB9Em-PbcbfZmQG8WVNC0-gEQuPkMiS8dzEewCVbcC8DhGGNClfKunvW0PvnKBLVVjljYI_8XCkLtM4z3u0wcE8sOW4gnocmQ1Tv5EvsEAGVHY3KeUD89T0VS0C7dIhNdQUOddKgCFqd_gvRY1AM_51tHk5uvYYkQ8RZEA4UwCzbg_Djqy9UNySR-DsHqz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so5DRAzHABeNmDgjaUfupBdvh6oop8vm7VUHLwrSJf2P2YyPRpojZtOXAX1Xs-J2jBiTRqborMx60B_U4-DWJBGDOIviMWzBe5kqUKunM_2zcTR6r91TqFO7ON4b0lBUKgoXW65dK6SvcrJL8KK7o3aOewZbc9Hsr838p_ENYDlR7JlnjfO_hlWzyHy4uolgi654i7eJjUTL1RDneE7HtdoosRWlL9j8bT55D7qiY5iL3wd_skChXmCfjyHLAwThalreALPMYLHRcxymb1EGzj8e7Qc65fhtKi4sX9gXPq1i2M3JJJ3095PdX6NmEV2ByVgQV_9wByaumEkeEdgypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFrn08XmRqoeL-hpDKO1noZ70S65aY3X3OuYnc4lg3wRXfVKew447idZLF0hRrYyQuVcOOXeDTHl_0NocWYv2XuST1H-n9rfTd4vE0977FiGi6B54tamQ4DI03nkWPcvZ1pV_A1DFB3yLwM4RiAy321x07nzRg9GM56xLLbtiLkgZrJFcqexw_DRq8ESg3KgdiixPS9ZgdONOnv9UPHa5z_sxPZ0D2jbiUrU-b2PhHoPRRs7b9nPmunebdckQosKcdTggt8quuW4RiI1aB6dke9P7MAliNwozjrEKfWyi6MEG58gNHMBtvqN7TZb3KBYsKOVgnzu-7l-uzZQiox1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awDV7vf8SIr0rYEGF9TePlJjwoZzQwzuw3XkJduL1A0MvaZbp_bVwKDsQFhxccccKJ3TBJFqmMHGFEi977JFen7IjgnGqBVo2u1t3HUSz-wt4P7FIAYv8i8CKDQI-6m9AcE5Q4f9kaWElP_b9mS3ETJVZFgViPrANb8sbEf9x6cC8846Sf4n-aWxG6iBZpPRCZlCLDczitob2ZLkK1CDtOK4RSXZMDVZhdkgjsNFy-FFsdHgncsbQajGnNL7ETWR_38y5Zntf_wLQRbAreXvxwkwzEp2huI3DLG_Eb5Sjb-zsGoGazkCTtU8yqJOk8DrpCfEsWaHCQhSqU3hsvK88g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBkBBZT26V8v5hNKWZV7f8rCNLutsJY-nd0BlhCBerQpnxJ69fQxNrLFTMkbsNuEUz6My87k_SMROl6WE6j72GyfTFTelg2SzLrY6BksOvtLqsiTaFrnHCSHpOVXflKxXch-PtZb7PEQo-C0X-4ClNzaY05c4-3L0T0iPpfNj-vDvzJX5x6w9plBP7WZbaiiPjqz4HVpW5pLAgmJD2glWl4Bb8JuDkVnkFnuXUZUKkP3k-j1hR4u9j8SAzSPIBk1yJD-dZX_cF0pECJ5JdChftr1e7mVxwdHZq6aoV98wcIhi0Yx3weVfNMHHbQUOOYatcuk0LZ61frGLFpm23KRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDNbpNOwxDPKCcvTPM4DnDp5UBtM1j3Jjrt8VFFt6svzgd8EouatUXj3nUesZ5gvxiIR1MHeo1k2AQhu1ZMYz_0r2aUbj6OHziKIgnSH0OG7KKvL_2pBZAxFlsIZ24HqeKdlZ3033nZY3teYTSvl7AhYJ1CPlwbAcNyoRaQfo--J6ehLtt27ypD8mEgQxYiXlwmZYLT20sayohwTbz5jpukeFBZelGHKivYhg53WnMR_hOoTnxJucd0oRRgofqEXYs--RxQYMsYnhmKsqm06eOMDQjU56Sv30gtC5KLFacXoseH7GZPF6wC92lxQ_dJ6NLmmvQEToujKj-2cXAXc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvHbtVe8oP_pI9gzjQ9uuDPmSPL_FT2LopjXnI4v4aYpBvM1lrBi0fbl1GbXNUgMQgzdxu3ND5YISsz-wHjYai-qLPzRz1-K4PBMbANckxRWZdfr_CV7DeCWpbq3B8NRKCsmSxNY4W-STSkR67dU3LZ7fwdi9vk8b_fwGOc4JPRVeJ_7R_dk20eWMiGsWd-SIpQsZ4C9a_rK1s0ra2_ENYBZYtHHe7IjR1uvblcegl0psW6cBkYvisSEMY2cSMmhyxb_zDy9QdK3zhzW6j_nDRQM1-xMr5HMwmCjir4vwbzTk6zJP5l-ttnXglxHsCeHMFPE8pcfX54lScx46vZQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChbASg6q7XVQAGgazrY2FV1sRCo8gbPu8DZNidcpn7UX-sBs4e5M_N8OCK96WGihUTLdTBcBH1E5AbGc6a3JarjzbHfl771OcEAx60TWBOVCFI_xeRte1Mk9xeYs8W4rNpY19PAEz2saYKtonYNpnT7YYbfI0S-JGTWq1cKxGZ1POX9LSgbbVBnO-ifvycOnht3fk0eZyzjDqCn91kvgJOXQUdOy7qVIkXiSjjt-fN-FwEmHl-ZpLM6uRiVFIBMXYNM4BAOxksXBQOpez5PWAcDVRQGIgyKdb_D8WuZ8IAnVQxUnNSPOt98iYxKrLtFB8-Uhb5Vu1vP65qlk472_vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApUAq271iqo4qnVXNv1wkWro1Z2XFn0qqTOn0sZYPcQfd2f27b14JKjNlb6rpEmGBqwM-DpYjtObC1TLIHoRaGHdLCwDUs_7X2oAidkE2IG7qrdnCn-gicfCt_Zx5yq9zNBya8zLQondudqaEWgeKPquoL_OP6EBeaP8PnSQIZ8nymOTSrcJk81ppl8SzNyV98uKRNgcMCglP9mAvbugXrsRPeRZT8tsByHcb1Vzxjxq4RMELfzAdjlKkg1GhbU6Dd8yrD0zRX9L68fMDvVeJi1xbz3AMaGnIpFtQlpcS5k2dw5f1bif8wKgq6S9jFh-q-EMcbF88EQXTZ0C3jmwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAfx7_l4hxtVZbwS4Ac7niEnog0I5XwBknXyMPiWGkNkjQZ7o0syTYOIIkLHumoJVaTZcWItkA175vdh9Mb9dwvNB74ehoCgUjKpiAwaZ7hsGK80E8Kr159g9CjvDeYhxq5mIGrGxvy7M91AteZJEAk_GVaqWu8p4K1D_1lse4WRioNr-lS9VbGhoOmvDGtK1bPNgPEjj6oKU0fsiuULp_SKwF7Xxfy_FGtWAte_II4RqpaapQ1Q_FVy8OKTi4zvhJYlkUphCeyv0XOXwb6wzfxQI62kMDEx9pjNQSOOunroUOxY-TblGX48ccjsxhtOT6Zv_dvjts8VhCqT7-65Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHUSnzmpI4jjDZzU-cGi5V32-EL2kYj5LUpkuj-y3HIt2qXLP45jWx9DU1RebY0wMGPZGAnwFcXjM0ps7vEy3hBjtgrjnmoqOvsMuf8zGAKbDFSiru8S4DNebA_82kM52GYm5jawB4YedgR9cGZgA_qpGdVp4vRt-lOxeDS4ivsZ7xHDGFyx63VczpDwFvKjSnYlhxcYxQj08MHKQQFgajwATqEnrhmOr9SPh-AGHLNFZ8i1D4GpX8Xt9flFdhlHwI5sXkUGzlfv6UkEWJ_HafrfVVK3terX2VJaeSWp-NI7O5nTAk5uxemV5dzcO8Fg2-nEB5My8_tfx7Rp8H3q8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4x2uz6rsB9I_eF1LhJb3AbCx2h9d54Twxa95jnPDN5_ydHz18cCOydq8dX_altUROf5pK8mFdi0UAlyT83ktAKM_duzs241qp7kcj8yYwwqHnQ-O6Vv7NZ2kQ5IV2UCrxKiZsgA8J1L89JXfex4k-qxek_-S0-x9wKP-B7j990sO2Z4CTgCgWpKXZvDqvYXEzyPIasAPnfR2T4y7pdgFqk9AF-fHr0t-ohafd4A0vBzAp5m5qQUYGGpXJ3hDxuGYsuw13XR2A1uyfRwP-T022PmYMJIIOd9X7X8iKVg_H7IBIVWgfpE-sUhhv37ubMRs90nZbDSVqT7zKRRLS_s1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv7XXo7mtuKAMBAdhvc8iB4cZCf-Mhs8KYgEJQWijiuPgUG-is0WKw9NHLt3K8WLMotmIejpGcEym1IB_Lu07CI8AB_GkKkbtStd64L1j1IpAUUq-I9dMHlCtxbQIjJzG0TuDh8aJwrJ-vwOLL_y1favBrfM_3VF9SbiP1IXFgzsnPMzM8su4g9P64ky34SUDa6KIEmkBYR9PjXuDGj8peCTYRJnGW6cXqxLKUpJbmriAKYde34UndnGIHup_BaTdNj-bvsGdxWQKaU92kEuLgyqPN9FiuwapsQgL7dVw4IX4JXWHvo4UonU1GaQyyUhjJy6Vj_9UWDbjSRu8tXb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1EJHCshUIvI_KDNHEZOcfot5qXifAy_Gy4TSCITu9HaaUgbwuFUChtD4ODnjXKVVQLOQrYiYnf3A7JPelTwh6SykKZ-PHUIBMF0P0x5MPEBotoo7na6Rdr50HfH4sr9HkoyCDOrFf4rrTTzQ9IfwOLyAsAdq_vm-WqgjNUMcYJ9jov1yLvVBfvYzbMFUeZhEUSdrzg3x7aDPE1IZMbQb3hCge5EOj1fvPXkbaOwXrfp2OrJ8Z8fP5xNNwagUstOC75VXXGV223U_vW40BGXazW_NxMLtYaH_nyDd_v6U3L53Q8Y1BuqBihtWTtM7Sc3nm5y6qNhwO_g8ci8cPLOLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
