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
<img src="https://cdn4.telesco.pe/file/dZgscLsOJWDZJWaENpraM0Vmeti-gSV910qZ7AmchnSSzfgu5t1fm_WcOp3yVF_zQea3eJPGaBK8R2DKsUmTSgIDeJPYpYVEuuNTj_7bcUg5IPEm-j_uEWLBQIV9zNWSygz-zyE07ICylBZK_R6TY-s97Bz3gn4BFOo6kMM1udyxh3e23EYJJoE2Xf1T8L5xUu-C-gE-iIpYJUJWe4KKDjp_GhKDA0sZvSV_ULbQFGUI42J5CcOqWPN-m79qldGh451HsOZD4ELIgHcycADi3_PYervWGfulEAKfj0FTWjCwHtI5XFIO3uJivAPewBXS9xP-VVDdTYGaJArHWm99YQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 215K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 20:12:33</div>
<hr>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=YdVFFGXbuGn3SnZrpmnwSsiSVmS0ZtltsLbQ7DLbM7-KGJxZOr_6gXto7KdaeRUI-8WILn3bj2ddifVrRlXpYVhuFG9RwsGooP-AIyK1TsnHhCqPoBvcKQZgxQZcgS3sqnWRZwuUFEo-YrPHiKEGEoa5proFsCPciQGjU6ZDkMh9Pwoic-sd4BBMEOIzoOs5x1tExvFKuQ4HarK8hxbGMxhHPeILjbXKwU-fdMFV9boteggfkVylzYAKwJ1ak-cEpIh4l7wIYxDQcZ0yL_ZGgfJ1wWkBfTkSFt1cZV7x0uIWU5a9NvhWs5ARfv6SOptzU_i6L6VgIm3ymV9u0TvMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=YdVFFGXbuGn3SnZrpmnwSsiSVmS0ZtltsLbQ7DLbM7-KGJxZOr_6gXto7KdaeRUI-8WILn3bj2ddifVrRlXpYVhuFG9RwsGooP-AIyK1TsnHhCqPoBvcKQZgxQZcgS3sqnWRZwuUFEo-YrPHiKEGEoa5proFsCPciQGjU6ZDkMh9Pwoic-sd4BBMEOIzoOs5x1tExvFKuQ4HarK8hxbGMxhHPeILjbXKwU-fdMFV9boteggfkVylzYAKwJ1ak-cEpIh4l7wIYxDQcZ0yL_ZGgfJ1wWkBfTkSFt1cZV7x0uIWU5a9NvhWs5ARfv6SOptzU_i6L6VgIm3ymV9u0TvMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=u6yLzMW0FIlFugXaN476XM-9Y-9U2ikHLmne3vpdT9sp4Jgm46xVZrvdMwBySyI5q7Hhpxj2SfezHpSZI_AsFN7lpKmoSiDqQ3X4eFXeqagYY8uq46rZ1xQMaGEITi2ulEqHOJaCTj5th6zQGQ2srb3caYSqBarjkeFCS9OXGe82cwUkcl5Oic9puslo1glcdzclP7nPYEVoeiCYhI4byVFrqnO9rBllOPM-uIS7IPAN0amwn4z0nohl5F7il3JlAdXU8sdrxeaA36g7Df-dD7G2Zn0UxJaLYrvyOsN37wBbC3HQrvgM7biFrGNsK11UL9NlytSEbIfaXxcyrzpKOaIvdZZqFnowEZrloLWKMmpHhb6YjWNEFg0pTRedWFoNcfAhMrct9pMtQrOnPWSfp8wn26lN5wZqCINYZzJZYgxilWZGVQzYn4zU__p9WXsnvFh6ci3a0w-yU7cPGJWTHi5xB_GfB_dcyI-FvIRpaEZFCSvukSlWjW_Mcysevz9oWQ1cgKXc6vHFbW0nRAeMOu_UWwOlBsVgUPm5p979bNbZ1A4oJzRjfqpm7Mq9WooX7WprgRB4T0Ka6W66wgQiEBXqnGZQ5ImKnTm9z8C9N_B2-b02iM_LZJprwbP5pxxl1v1RFxpDhOKMedtWzXRnmRiSMqxXNhUew9PbZWIAVoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=u6yLzMW0FIlFugXaN476XM-9Y-9U2ikHLmne3vpdT9sp4Jgm46xVZrvdMwBySyI5q7Hhpxj2SfezHpSZI_AsFN7lpKmoSiDqQ3X4eFXeqagYY8uq46rZ1xQMaGEITi2ulEqHOJaCTj5th6zQGQ2srb3caYSqBarjkeFCS9OXGe82cwUkcl5Oic9puslo1glcdzclP7nPYEVoeiCYhI4byVFrqnO9rBllOPM-uIS7IPAN0amwn4z0nohl5F7il3JlAdXU8sdrxeaA36g7Df-dD7G2Zn0UxJaLYrvyOsN37wBbC3HQrvgM7biFrGNsK11UL9NlytSEbIfaXxcyrzpKOaIvdZZqFnowEZrloLWKMmpHhb6YjWNEFg0pTRedWFoNcfAhMrct9pMtQrOnPWSfp8wn26lN5wZqCINYZzJZYgxilWZGVQzYn4zU__p9WXsnvFh6ci3a0w-yU7cPGJWTHi5xB_GfB_dcyI-FvIRpaEZFCSvukSlWjW_Mcysevz9oWQ1cgKXc6vHFbW0nRAeMOu_UWwOlBsVgUPm5p979bNbZ1A4oJzRjfqpm7Mq9WooX7WprgRB4T0Ka6W66wgQiEBXqnGZQ5ImKnTm9z8C9N_B2-b02iM_LZJprwbP5pxxl1v1RFxpDhOKMedtWzXRnmRiSMqxXNhUew9PbZWIAVoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=pTZleJ4O-YnTke34vt2LDWdZ4JlnC7Gmen3tB56fTkVVhCX2QQvX48fmpbM75avOdOt8E2AM4tuaqBHUJTPpsM1SxRgLNXRo1qhwKVugskbHLvD4kefTZn8UhrkNU_kmVVstOiz2BWNIXptW0ykNjQ2UosNYn5FZugkYze8jJJXYbLZ5Wl_vEVU3hsl_cqnqTbglOVWrddFoHMrPCi6ETUJ-CS8k3C6pEMH05xVQBHeg1KiOmcwQqmKOmOLt_qiqmrb5p-_zRSRS3LkGtCggSE9oDtPHN1W0WL0iYZ5lg6vGcYOZFvnOrhPxKgEq66oJdQdpjvsJfdvdoEP0H91DRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=pTZleJ4O-YnTke34vt2LDWdZ4JlnC7Gmen3tB56fTkVVhCX2QQvX48fmpbM75avOdOt8E2AM4tuaqBHUJTPpsM1SxRgLNXRo1qhwKVugskbHLvD4kefTZn8UhrkNU_kmVVstOiz2BWNIXptW0ykNjQ2UosNYn5FZugkYze8jJJXYbLZ5Wl_vEVU3hsl_cqnqTbglOVWrddFoHMrPCi6ETUJ-CS8k3C6pEMH05xVQBHeg1KiOmcwQqmKOmOLt_qiqmrb5p-_zRSRS3LkGtCggSE9oDtPHN1W0WL0iYZ5lg6vGcYOZFvnOrhPxKgEq66oJdQdpjvsJfdvdoEP0H91DRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDJsvY-k3nQIop3kZT_kC77Fat9Mw5L827i1q2iH6STE7m1C4SqKsTLKAowN3o6jE_foJ9Ur1Bcbs3BpjpGC3Du-xidc_Mx2QroNjumzy6e_TB5Ppjgs-L0O8XrZZh-MfZAn36qJk5QDxYQX1VtiGdqF_PcQe-gbz_WVst-fKsh7fxrg1fxHh5kOXtsPUSzhx4i12LMH2he5Z5nwKW4W6Xc5T6i3Ea4MDPpmAjbPMJ5Pc_JqnXKcO1ekxxgSbxmDP-GiuGy0yZaBU24Kik0bi1O63fKjtReqmvkFTQAPVmyKQK6L4xGBiBa8lqseBQuA-MSgCqLn5mVQDtCigd35SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=BviUrXP9ErR23H58UynfnTn3cXI6U0q-dsGpzvBJ9FjXJV1XiZ9G0HvIiSsP3n8QLJXln9F_xPlcGQq-B6GwC4hdq-8gimfPRMbZH9vq3eKYbv2nkY0edVDs34VpGOGH-teYpCDnzmpB5wddZ4j4FKXhRjmEcRNdrdkJgsSr3SNmWhQtopR8N4EitbHk8Ft1YjOk3ZH8UohW0l5mP8s_kHO6femCwxSVep_AeUEgRLGfQlhXscfKPpAE_llABhWPv8qP28D1OvEXTO36iQ_Qs6oflif0uqODpFHTf0JYwZxVGLGUSqAXTioa_DL14_JsTW5jRdmPZaUdezY67bttLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=BviUrXP9ErR23H58UynfnTn3cXI6U0q-dsGpzvBJ9FjXJV1XiZ9G0HvIiSsP3n8QLJXln9F_xPlcGQq-B6GwC4hdq-8gimfPRMbZH9vq3eKYbv2nkY0edVDs34VpGOGH-teYpCDnzmpB5wddZ4j4FKXhRjmEcRNdrdkJgsSr3SNmWhQtopR8N4EitbHk8Ft1YjOk3ZH8UohW0l5mP8s_kHO6femCwxSVep_AeUEgRLGfQlhXscfKPpAE_llABhWPv8qP28D1OvEXTO36iQ_Qs6oflif0uqODpFHTf0JYwZxVGLGUSqAXTioa_DL14_JsTW5jRdmPZaUdezY67bttLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=TgTgkXCCE0s0AQZ3nirTu-6KvzCqbSDPJMh3ewQn1PIht0UP7zuAaY5j7LWZlpO63rrzXO4Gwj-1MJvwjfgaBijfpd9x-KasGnv8dPQFDGlwVSlh6F2EelkaZA5OwwMKOcZUCS83CZD_gjqJ9FL-I9lJkzICa4ofVS07p315SNfebtJ9Jesq_rNzmB0HpdPru7uGGwoP7cB99RqUA-00U7tQxdFQfkyV1blswp3RRe9mU-Iu-BqizEjhkP264EndjxwWgCSl5VpDvalwmQECWnwnQyQRWpkJkxSpEzy14CorXxUEOYAedjLFnHABnFtCKBCg0VPJhuQ9A9xtF29AYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=TgTgkXCCE0s0AQZ3nirTu-6KvzCqbSDPJMh3ewQn1PIht0UP7zuAaY5j7LWZlpO63rrzXO4Gwj-1MJvwjfgaBijfpd9x-KasGnv8dPQFDGlwVSlh6F2EelkaZA5OwwMKOcZUCS83CZD_gjqJ9FL-I9lJkzICa4ofVS07p315SNfebtJ9Jesq_rNzmB0HpdPru7uGGwoP7cB99RqUA-00U7tQxdFQfkyV1blswp3RRe9mU-Iu-BqizEjhkP264EndjxwWgCSl5VpDvalwmQECWnwnQyQRWpkJkxSpEzy14CorXxUEOYAedjLFnHABnFtCKBCg0VPJhuQ9A9xtF29AYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Y7EZ9AHCsqQj9aXeSIJ3ThS2Vk8AA3DRJ9vhovHCGVzXTtcYIQULzng4yzJn6Gz8c_AYiS0NtaCFhpf98e_EPnHKeSla0Lh2PzdeBpdmDx7P-9VWCWeyedFPzxmw1y7OlJhgEEaly0xUyG-5XQg3d3H2CIxj_VWYeb_0a-EmZQLEVcqPfmF7virdiLOK6p2wRzl6ZnTSVTJKOJRVndzywhLp8gUmbh0KnjqBXSRPZj9uOFty74ZhpCs0pG9Pzm-Y2Q3BfMxK9hmvfZfX4V5M8UbHWSjS7ZFp6zzDU9VybMxOc2nqJ7lc-9tgStTVg6cR4sTCLDDsD5wTRwPa_zFmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Y7EZ9AHCsqQj9aXeSIJ3ThS2Vk8AA3DRJ9vhovHCGVzXTtcYIQULzng4yzJn6Gz8c_AYiS0NtaCFhpf98e_EPnHKeSla0Lh2PzdeBpdmDx7P-9VWCWeyedFPzxmw1y7OlJhgEEaly0xUyG-5XQg3d3H2CIxj_VWYeb_0a-EmZQLEVcqPfmF7virdiLOK6p2wRzl6ZnTSVTJKOJRVndzywhLp8gUmbh0KnjqBXSRPZj9uOFty74ZhpCs0pG9Pzm-Y2Q3BfMxK9hmvfZfX4V5M8UbHWSjS7ZFp6zzDU9VybMxOc2nqJ7lc-9tgStTVg6cR4sTCLDDsD5wTRwPa_zFmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSfTUN30H_OcR1kJxKly1chstwYJlES1lD_3V46UsGz2OClU1IVPCVqRXeegxwGVo6AKyOb-eMdfteEsM552SGz47y5l4h2Ey_5W-HrdhtFL1YG0v2LYwWxiHMFV5sNN46r4bgby17ZqvDaztIt2p0Y1K0Sb3lYz6bN0SDHbcnTG3NPvCM_xNpPv50oBthHEMgNSfLEKKycEtEgBQlJnZnFXqrYmGVeC1IiRGR_kLrzN7yPW7b3qXnXv-Vt1w0B6CnkX031JM6KtYZttwWyf7-mPf1-q5y2icPo7k923jq9qbTySEx7xxY3rQSquqzR0WV2k8zO29NxJlysDGGz43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=AQYcS4U2-KJZG2666sP_-BIK3DbNcBj5Ss1oh84J_MbhlnCt64rS-nPU_eKGYfMMSgJHZnpWxmFlIBgdbPvYwMJ2kYhJp9o5i6Ymdm44QWjyHz-nSS9cuwc1V7CsWEOLPu0cjCTmctQtuioZKf_M5qbeZh-PuEoiWv6daj_9xrm8mdR4GM6p6z7pYxJItrrAzHmSafUixTDDu7_mra5x_2TPInHdury4Cl0gXIoo3QnawiymSwZeiSUI64naF8-jz32XTFrCbOeV105Z4JiXt3MEMHl6DqIW8a8UpKT7_p8P6r-Z8jWvOJaXWc9NqESM_btZEj62fVAITEJeC0Akyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=AQYcS4U2-KJZG2666sP_-BIK3DbNcBj5Ss1oh84J_MbhlnCt64rS-nPU_eKGYfMMSgJHZnpWxmFlIBgdbPvYwMJ2kYhJp9o5i6Ymdm44QWjyHz-nSS9cuwc1V7CsWEOLPu0cjCTmctQtuioZKf_M5qbeZh-PuEoiWv6daj_9xrm8mdR4GM6p6z7pYxJItrrAzHmSafUixTDDu7_mra5x_2TPInHdury4Cl0gXIoo3QnawiymSwZeiSUI64naF8-jz32XTFrCbOeV105Z4JiXt3MEMHl6DqIW8a8UpKT7_p8P6r-Z8jWvOJaXWc9NqESM_btZEj62fVAITEJeC0Akyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=n8nLRibO90FhVP_XPk792WNZIyVctDAXkluffn7eav75bDK2qGt5FnrQvJwgncd9EAHBbjaAUw1pui6sgFLUVhEXH8xeuS4_IotIffnw2YCWSccvtPYxFhO5NzEcsC8Lulm-U1PuZ5qjd6KcpSS0R8XeBwFW6akRvPZlylTKoGCJVa8Uk4SEMKQ6qGOn85oo1UpuaRdvc1t8X6BZKOUhKKu35VcsJDI3xkfMdNRK--ze0gU0LvSBNgkM4prU7k_y27kROlTGCKHt7oj3PCQb2CF4QYOni2mgEftxQf4HTH27DJpJT30TVuR0QGY7GeOvxHjLlvsbe9yJly9Umo65OA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=n8nLRibO90FhVP_XPk792WNZIyVctDAXkluffn7eav75bDK2qGt5FnrQvJwgncd9EAHBbjaAUw1pui6sgFLUVhEXH8xeuS4_IotIffnw2YCWSccvtPYxFhO5NzEcsC8Lulm-U1PuZ5qjd6KcpSS0R8XeBwFW6akRvPZlylTKoGCJVa8Uk4SEMKQ6qGOn85oo1UpuaRdvc1t8X6BZKOUhKKu35VcsJDI3xkfMdNRK--ze0gU0LvSBNgkM4prU7k_y27kROlTGCKHt7oj3PCQb2CF4QYOni2mgEftxQf4HTH27DJpJT30TVuR0QGY7GeOvxHjLlvsbe9yJly9Umo65OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=k9-7fXupnsW6ab199FL12jQbi7qwSDCvJOs36cglTf0gg_06xJPDs7Sk2yAItGajoLV0OQAlqInwI3FDV0_U58flFLLiNfCZthYgqw3vRBHR6CAPJveqlRBM8tezMO9sydD_DQ2kw9nGMOFp_FvXmFBBni_tTZAWPcSNbMWfH-JXm9nEJVoQDmfHo9d8styx9A7bfxgjEaFZzGlzl2J_hL625BotYKGflyCE-2s_BTrTerwV_7SbMwJJji_pBu5APaPINGyK3-JtQ4b-gzaxsHRR0IBlHX8d4oefGjCSrjYyTBVi8fN1pdKFHgQQLbacPNd0O74vMWpQNDImc2iolw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=k9-7fXupnsW6ab199FL12jQbi7qwSDCvJOs36cglTf0gg_06xJPDs7Sk2yAItGajoLV0OQAlqInwI3FDV0_U58flFLLiNfCZthYgqw3vRBHR6CAPJveqlRBM8tezMO9sydD_DQ2kw9nGMOFp_FvXmFBBni_tTZAWPcSNbMWfH-JXm9nEJVoQDmfHo9d8styx9A7bfxgjEaFZzGlzl2J_hL625BotYKGflyCE-2s_BTrTerwV_7SbMwJJji_pBu5APaPINGyK3-JtQ4b-gzaxsHRR0IBlHX8d4oefGjCSrjYyTBVi8fN1pdKFHgQQLbacPNd0O74vMWpQNDImc2iolw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=Nsz1YdXkxRtLIcbOGvFRnCwGGqwPCeV01xQcmFIYR0acdYtKe7K7Pghu_Ktot4fX_o5Tg_EByTNhfy29e3vMqyGCfMgQn2AzBZtJo7IySvo035F8nPhPY-iTwUJnNZeDoMhZFlGM3q6qMr3sOkQTHsdsrGWW0DPptkUdZYSK32ONKnrJR46hJ8l0Ug7ByphOwDTTZeaIwzCVGcgick92LtfK5NgwWPC-FdVwkD7xKLAbzj4B8vW7hBIZkX3WVxr2VlSpp0fQelKzHUstkd1vLJdKvVXSVX15WUEFV1NgXGxqaoIwDV2FSGRlW2eyH8LabP6NwrMLO7FVxzzQtFSPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=Nsz1YdXkxRtLIcbOGvFRnCwGGqwPCeV01xQcmFIYR0acdYtKe7K7Pghu_Ktot4fX_o5Tg_EByTNhfy29e3vMqyGCfMgQn2AzBZtJo7IySvo035F8nPhPY-iTwUJnNZeDoMhZFlGM3q6qMr3sOkQTHsdsrGWW0DPptkUdZYSK32ONKnrJR46hJ8l0Ug7ByphOwDTTZeaIwzCVGcgick92LtfK5NgwWPC-FdVwkD7xKLAbzj4B8vW7hBIZkX3WVxr2VlSpp0fQelKzHUstkd1vLJdKvVXSVX15WUEFV1NgXGxqaoIwDV2FSGRlW2eyH8LabP6NwrMLO7FVxzzQtFSPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBczA6zwqKoD-SIOPC3Ukw5SpYf16Dp1K2wcb_LJUEprG1F7PJTE9IfGP82udCaVc09RBlhKCuEhGIXFwllEc3kFWh2TGahirV5-iU_uve5V7loRf13V_7ImUyZhjK39oTGfZW15t3hH6wNzNPf_hKUBTOC_k3FhLNS69pdcbK7TlSd8-jmBtZ1bcEDOltdCByyTmc6Cl-0-wHc-FeVWCcTvsruWCYKKBjjAWqG_uY0st9mxuq8EmrywMfYEUw3rNc4tIXs8Pw--6UsegRKsGHuCvzMC9jR9Omolaov4e3vgRazPtvVugc8hSiCLiL6n_QMqnMXL4sMlGypa9P2JfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m790PfDEyPG7z95UebgSPYDB4mMWtOjzoBxO4_FAEH_w15e0zPhRUSErK0unqq9JpwGaq6x9rLfMnPxWBufRstWmPzlrg7RR_TllXCsPADrVxXD8_J6y6u3N0drA3ybZdYlGpKjDinRpaJHlEF-M3RkMxVqgBKCTR2ng2WkeAm5q0HYMxAw5GHBdRiuBg7NMqUNZl7c4n035QTyQvhJxuQjNjw52xDex56r_21DFUhWPzUzNISAjxANB7EcYWWoQYbvgkoXdhJUU9CjwBpnl852tCUlIoImwXIsDlw3O8iFXKRJjOd0iomOo8uGjrZ1Nx5ouaHhcq5dJxPCQ4MxxMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvIfb01H-0LAeb_oAfAGusg3T2cDUjVu7qqVuFf-MpA7WckJvU-s1Vd3YlKaQ_aW32010Yms-X7jTHOzDho6YyxY5Ip5ef8dnAHFZqv_moJfhT-nACbUXUsiTd827hxsEy0p_HhRCdcwwzxKGeaXQwy2kmQmqetAiJI1eHIbSvpQGilwabO61_JHrgDlUydR2XAVMefe8woeVKMmIKAEgLVhUuhAdW3DygAbj8WQC00aZL0yBstSPqW7I-YtUvCLmvMvHubKqv2q3BQVQrc7GDOrGWhgbPM1bHm5cJj4z1CoSAs-kQT6ZZ2BnWsAmVl8jIZ2RZmapzbWtUK30fttDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBneLo0u2_UOGTmOUffr4Gs8sG6hESRiaDftGYLGCQZJDtelqNeZLjxXIW8zbdPGplANGtRQ0XFfJ9lmUvjtOtABR3Dwv6o81neOduWi7HgyrwlvuzIeW50Xhlc4zTobavks5SHJDcIsKKrvHrgmuUHzs_FY7Y9TkvnCG3nuPrkEaIJ6CZsLpiLHfg3p1TapK_3TzlBcwiBKkK7WjJWLjTG1g298dfGNG9SmQR_GVy1DRLM7iouWJUKtdzMWlWXdcSRv3WfDqz41AqOzHeF4rLOaO2EQaIqBicGbPGGH3rDfi_KigpGc0NyujrYsKH4ceSTciD3mHN2d3i8PLpHZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiKHhF0ELrnyr79vcU6I56haCbVVgKkE4ylh1S2Sf_2FzHd44SQSA6e7E-xXl3BpgRLwxAGdr-zqcFqA_6M5Mx4nGabI_-zUypaD6Mz9b7BTCRxxSjnAVl6AlPQ_llghjDLKaSkJdbAzYKtpQqPZt6U2pZC5Fx1JVo_bu_2jkoLDy4CuzjMV3GM1fR95O0ThEgDcoIMMrvNGlV8VYTMOLWpuEnYPA8prnNiQ8Q16oCwgkNTvSIGl9LwPZCNrcU9HsMQQxc3_W8JVuZPysh1O9dSUrDHh9fW4lsh5VhducsV05KNBg_xVwEWus9Si5WdD9Y0pggWJ-TYYUuo5JXfvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=KTTmAQeYectZQw8D7CfKAsKkeLrqO68mn-q7gK3lkJESfa1hi9KghkiRI65N-xVOJ7bGL5LtK20xVvOFKikzDdzH59LR-8ZVRxlMZ_dlxqMx8O9oMrlUfjB88MdnGsKyyRxyOnOpiQFRLP9Ua_IU53pw64oG8kuS7j4gmcwdsAsZdDPjgCiySTWyInIqtC_-sjWDh8GdyiQP3EZBcBDQ7TO0zM8WZ4XTyhEjzWmiEUbMdKBLl66K7nNJyLTeHXRM96R_PPTVVeLI6DYyqF5QfPKXgJeSq2K9nvNNvkbBtV-8tJOjSIKjMS0jRAULYTakULGu8bgKQ-4RgOwj2W_XRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=KTTmAQeYectZQw8D7CfKAsKkeLrqO68mn-q7gK3lkJESfa1hi9KghkiRI65N-xVOJ7bGL5LtK20xVvOFKikzDdzH59LR-8ZVRxlMZ_dlxqMx8O9oMrlUfjB88MdnGsKyyRxyOnOpiQFRLP9Ua_IU53pw64oG8kuS7j4gmcwdsAsZdDPjgCiySTWyInIqtC_-sjWDh8GdyiQP3EZBcBDQ7TO0zM8WZ4XTyhEjzWmiEUbMdKBLl66K7nNJyLTeHXRM96R_PPTVVeLI6DYyqF5QfPKXgJeSq2K9nvNNvkbBtV-8tJOjSIKjMS0jRAULYTakULGu8bgKQ-4RgOwj2W_XRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mVb3HlnkMQhTc4N6p_bEan74pVtaDGf59AHiOgTaVuoMC5ZynyNk_vGzfWmIPbBLMJf8R9UxNtOQMiNflzujqnE_u3U2knomt5mTAglh97yoNWcE_bSU5d6QSvxpzOCaPpBUJ7Q7wbbVxwTk_SCBrosQk0u6MCi5o-sP7ZdCklAYa09Qh43Y4a_7Iw6XjL_-tZCvoGLZsvIUrWBVauceOAbVI4E8VoeLsHlnj3ElIDSzONjGXZqsPjQzLfI1zo_MsCX2rdrs8y-ivpbdhdPbiBDOaLEF-PSfbK0dDxEin4ftxJRViyz1JbU-IvH6GiUQdJazxu9mGfoYaacMb-xl-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe6NBDFT2yhxoGK7f83jXn8gI3ckx1I9MsZNrl6MKVVKkQBv4x8zOAtOYbAIQ-YApJgJMmBTz5EXWutPO2wtyx68t3Rrifgeh3apVQc7mu0OKuLl1_4j13D0EDClaXbiPazxRHIhLAej0ldivN9Qdy8KMIwsaSbgYeKYyUlOukAHs1yUAfJjcl1gtmcNseBppNNz3-8yFjxDcFZlCW4uh6ML8BKBXlDSasQeJrwo1UvJfPYbqvzjRjSnnbUW1gNizMifDJ0VxLl2YqAIHou5XLj4p6JHk7qY790etdwsAL53zAMdF1tEAEZNfRcmcIooKAkf1lK4FiUyyGWu60WY1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=nAe_YE_Hlr034Ec4MjhooRhmyHkg1IHYi2jY-eTChzxPgtJDbrxlFZ17Eh4Cyq8Weq8phKTqEAoIKPbDZ1LCZWnFcfmFJU-GxE85uT32M_gXYmChRUVnxeWf07MAv-0BZxAF3ET-bm0_pUyZgPOAcPHEsAVYx5lwB90Ne8JzTftYs_1IF5QiftWB9Po-CVs7Zx4JUDE6j4ZXpLNSjwtXMvezPIIdvCegOk4pGFlJWsq7Ui2QXjDerWewY-H9u6ejn9eEiUIKj0Q5uClibNMBWuAyPHoscQ9zk71WnokZskCSS1_mwK7fIGdLZ5lz3uqg4J9WA023jkPA_gkSMaVG3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=nAe_YE_Hlr034Ec4MjhooRhmyHkg1IHYi2jY-eTChzxPgtJDbrxlFZ17Eh4Cyq8Weq8phKTqEAoIKPbDZ1LCZWnFcfmFJU-GxE85uT32M_gXYmChRUVnxeWf07MAv-0BZxAF3ET-bm0_pUyZgPOAcPHEsAVYx5lwB90Ne8JzTftYs_1IF5QiftWB9Po-CVs7Zx4JUDE6j4ZXpLNSjwtXMvezPIIdvCegOk4pGFlJWsq7Ui2QXjDerWewY-H9u6ejn9eEiUIKj0Q5uClibNMBWuAyPHoscQ9zk71WnokZskCSS1_mwK7fIGdLZ5lz3uqg4J9WA023jkPA_gkSMaVG3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=vG-sLO_A-_fLm-IQN-JJe6QF_9kQaaJfxazVvFJA1jerFkk7qhFPezdvQb1oH4mA6Pj2HwbvfYWiyOZEbWN6RrU-SlsIg4fCQ7Uyst7PleEPm06TOfbXJAGkx4fdJOFhlAFBz9r38L8XEgNMPRRXY_vI3pCRe9q7RONvafJcqaIm-RyY7b4HPpvL3-CaDwdslBizBTS46Sqle-vpa9HjYdRSc9i0Vueg_TbM5Uq-EM_dyztU9b8gAYELUSLKbitWqf0-LDhxQxCbv50L-SzSGQZfqftAr4j3j02aeHUOun5GZW3Omy6vw7oOgUCdtaXqvSp17LjJGeQ8mMCIlYbbLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=vG-sLO_A-_fLm-IQN-JJe6QF_9kQaaJfxazVvFJA1jerFkk7qhFPezdvQb1oH4mA6Pj2HwbvfYWiyOZEbWN6RrU-SlsIg4fCQ7Uyst7PleEPm06TOfbXJAGkx4fdJOFhlAFBz9r38L8XEgNMPRRXY_vI3pCRe9q7RONvafJcqaIm-RyY7b4HPpvL3-CaDwdslBizBTS46Sqle-vpa9HjYdRSc9i0Vueg_TbM5Uq-EM_dyztU9b8gAYELUSLKbitWqf0-LDhxQxCbv50L-SzSGQZfqftAr4j3j02aeHUOun5GZW3Omy6vw7oOgUCdtaXqvSp17LjJGeQ8mMCIlYbbLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=JK4LaWgpMYm0ZQ93MuTyctuHyztrv8v8W14019gAI4WzHp2ZqMIu56dZJoyoiA59s0WD2OypMw3hAGV2US-dk0_xqiCvHhpUKy6gf0Tw8-rGOX1m-sV8l-eJxHhe7jeJo4Ccyf_NEglMwFFBUicrieWNqmlsCFobhGN-JeyqR8lRPnj8k0tvGVWPRgqwfl2Yj8B1KjHaBRkOU1aomnzDmrOtU-Pj5nvsd-ibjpt7p9aeo0FKkeefnntaX6eSUTjlDKd_5KhEgSCz_Y9brtmxOriRG-5RZHv2bj5-zDyLkRvROMMBv_f5Bx9idi9z0YsX8q1uayVw0VFG74Hwg32DhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=JK4LaWgpMYm0ZQ93MuTyctuHyztrv8v8W14019gAI4WzHp2ZqMIu56dZJoyoiA59s0WD2OypMw3hAGV2US-dk0_xqiCvHhpUKy6gf0Tw8-rGOX1m-sV8l-eJxHhe7jeJo4Ccyf_NEglMwFFBUicrieWNqmlsCFobhGN-JeyqR8lRPnj8k0tvGVWPRgqwfl2Yj8B1KjHaBRkOU1aomnzDmrOtU-Pj5nvsd-ibjpt7p9aeo0FKkeefnntaX6eSUTjlDKd_5KhEgSCz_Y9brtmxOriRG-5RZHv2bj5-zDyLkRvROMMBv_f5Bx9idi9z0YsX8q1uayVw0VFG74Hwg32DhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=C2nOU_J-Bmz0S9x4QrZB-WbBNVgdJQS_iheVaBjwpOSoAsYsZ9KgxFhDvFkvHzMR9t1FolmGOviR_puL3juE8KZ5KV2tjhQZxh2WUowWfIU7j1a_M37yRU0vEfleMMM6G31OsRkXjy4OHgcTp9Xw8D5tLAlJtaBFxd9vYEOuOSTpQf0zKTNMCvHNXlho8XprLYEY8V44E936KiDyHxjx-GdT6IG0mkhhsiLVgdZX_wloTKU9Pjnb-f4hu4-Xj1ND_jJ3edp_fFvZ-HCAWLgSJemRVdpdmW9ngyZAcQVuhgP3Mj735UWG-58R1dyqSerMz1FPvAMNOfBdtB0jPDvcqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=C2nOU_J-Bmz0S9x4QrZB-WbBNVgdJQS_iheVaBjwpOSoAsYsZ9KgxFhDvFkvHzMR9t1FolmGOviR_puL3juE8KZ5KV2tjhQZxh2WUowWfIU7j1a_M37yRU0vEfleMMM6G31OsRkXjy4OHgcTp9Xw8D5tLAlJtaBFxd9vYEOuOSTpQf0zKTNMCvHNXlho8XprLYEY8V44E936KiDyHxjx-GdT6IG0mkhhsiLVgdZX_wloTKU9Pjnb-f4hu4-Xj1ND_jJ3edp_fFvZ-HCAWLgSJemRVdpdmW9ngyZAcQVuhgP3Mj735UWG-58R1dyqSerMz1FPvAMNOfBdtB0jPDvcqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=n06ejLTmjNGPVZavTUJ-ohZqwgh7j0SUINZcTrftMWGKPsJSwthMuxTRlmKeLXLuTznKabMuEhODNykg5wIjyRMspeOh863g62wndPdAcwbdhJbPodU0Sof4MlgnggiUtjsUBDlYFkxmxNJq0ZRyNAqnEyCo7ZVKl96cAHLq-IACkAgGL5rwy0GxjpPL_4l756oxmWQMsgmwgLrDTJmpeQ96jKyll8qjM6s0eb0PcYJcZNqcQS4gKxGdnaBW06SKan7m7H2Yq5z1bz0qyaa-68bgwU-23GhOoHfonsW5k4Ol_znxYT3Fo-QNGn_SSsDs2plZP6-oN2nErGSTCzvkBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=n06ejLTmjNGPVZavTUJ-ohZqwgh7j0SUINZcTrftMWGKPsJSwthMuxTRlmKeLXLuTznKabMuEhODNykg5wIjyRMspeOh863g62wndPdAcwbdhJbPodU0Sof4MlgnggiUtjsUBDlYFkxmxNJq0ZRyNAqnEyCo7ZVKl96cAHLq-IACkAgGL5rwy0GxjpPL_4l756oxmWQMsgmwgLrDTJmpeQ96jKyll8qjM6s0eb0PcYJcZNqcQS4gKxGdnaBW06SKan7m7H2Yq5z1bz0qyaa-68bgwU-23GhOoHfonsW5k4Ol_znxYT3Fo-QNGn_SSsDs2plZP6-oN2nErGSTCzvkBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAEhZ-T2rBS_IGZ78rl6UBftV5pSpSt_GZe5Mr7v-7cWIaO6laSGwqy4NE0d1kaHDkM9NWz95WawMhk0-4uWDodsYq2mz07VB8aOqAUZuVQ9aI5Iadz7z5lJ6JsiDw0ATpONe9JLwwEKgOMTT5wL-YZUDMqDfJ29GEO7EXpop1xMcfBIl5zqvMB9nNEvSqHW4Y9187UmEq5yvMYH8xOs6CMAZEIId0-0C8llhIPXgOtJvR3aQbYBs-9u6nsnBBhCo94MfyCzaXe4Rp5Lr4w5wCLvBqvPUi1BDpAX-xl3eDwO5251saPIMgUWZV94JH4qZbIDQ42nZS9louwjh47-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHj2DWeVmu9d20uZJS3RZY7a4xoaRjpVQOc1W-pPFnY9e8eBRotz6r8GCQgH_RTMFLGIImTMHFfix4UDvCNpPvwX4J71401fygBrNdYzRagDZDGB5R5YD51S-QW1oqP8rhWBpHyEMuw3jwiy57kI1rL4-ikjIOzlHL8rXJywL7RUxL6lY3K9qDl1aJ3n1X3D3SzGE4RLLE7pXivFbBGTmNvgmMBBP3_fI1506J2XljPLBKyaAYJxXr58IhZbXgCcri9_LYX3LLjSIO5mqFNDNYMAnUKAP4mVaEYsi-YtZuTifCiJ40Q1ZAOQG6K-c5eejXkm4KG-aeEnoF6--4BLGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uq-N9ly_V_ABU6-4qjrVkgiZ2W8lOwXLe93yt17HO7sbYx0aSPlNwN8gqGMLC7e3mUh2Kf9EIaa2RmyCJfEfZzSqyE1Y_kXNL1h59fltBqqUiHKZjYAkthEXc8CKzdNnT9Yz1RtvBuTezqFA4gmxEWWdJD0TYTZQL5mtmdjnPEucHDgVa-qgDVFJqu4G-9VRczyIsTdrcDjjM8o6xpqL2iV3mxHATAMl7rG0btxN4h3gqsQ0MiuJOklFPB22A-xDtR4rk9KvtG8h-W6-tb1vw-R_ETh7USwMKO12DCfXBHqBjiWbHAQgubdNNvi2Q_W9B9b8YLG6weIII_QrTt1RQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=PEH8VKrDudqvdm-6qmcR6zcRTzF3T9mIYayWNNE4HfdjVnfAOuc-ptUqjIk6PYpGRD7MGefg8gjFhCoctVInDPm0YftIUOUGwoVEq8aPHRBQ15GhHyQfneUPza2BSd0Mo-7PEItpBO93GhUJisFuCpPfw_tpFUpCD9KuOLO3bE5IY3Qqd-8DkM3EYduWG10YElwYpr6WkjB-USm7UU2KGzuIBEbYoWFGlZaKfAzEV7m_UiVYjXRo9fkCFrkNNNPoWZyANt32n0TOtbKgZzYgTHejFQ7gEKb-Utxs6s30nM2fNU14m2Ol6RA_d2XXNycgF-V9Uvst229VKkWVfE-QYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=PEH8VKrDudqvdm-6qmcR6zcRTzF3T9mIYayWNNE4HfdjVnfAOuc-ptUqjIk6PYpGRD7MGefg8gjFhCoctVInDPm0YftIUOUGwoVEq8aPHRBQ15GhHyQfneUPza2BSd0Mo-7PEItpBO93GhUJisFuCpPfw_tpFUpCD9KuOLO3bE5IY3Qqd-8DkM3EYduWG10YElwYpr6WkjB-USm7UU2KGzuIBEbYoWFGlZaKfAzEV7m_UiVYjXRo9fkCFrkNNNPoWZyANt32n0TOtbKgZzYgTHejFQ7gEKb-Utxs6s30nM2fNU14m2Ol6RA_d2XXNycgF-V9Uvst229VKkWVfE-QYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuFCqaWIb-tW9JXiI8HikKAUJxwUETn9e7-rAAevReBZFOhFTRoNejK7ZhddmprSh94k8n-UZyMWG0wmy2z15o4p3AxiqGr5Asld1K-yo784j4j9q_ZtpSbjiVxEaRzaoME-Md1L3MdrGuz0fqrKoyZCxPvKWZ_KrdBKWt0FF9Nz70dwlbPkz7QgILAbexPayAJj0ShCOsILI6gghaV0HS6USVMqnLGp-ouOdakgEg2ohNNtz8cM1RvWB73xqhz-8-cunx7Ykpw8jtEek81--bkP-U3Ty2Czb-IHAJajBcJVA2UOPJXG1KOwQexXT5Cmm75Mbejj5z1N8t9xXXFzrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=nDs4pOpxkIVMIKvkfs_ICj6jEjnTabhNDZMAgo15LruxiNzlzqXseok3V7ELRYjVprq-s1Bow_ynouYjC97s7xXXjPdRJnAkHtAOrieGq5sS7_UZ6tT0MrxG6ov922eRxaAHiBlO4Klkz32F9vcFzMR0cLzYf9j-tmGWFTU1STBqPf-mPLYKDH2ZjNBphDR7AfLMqk16bRAbf1akvXqBHnbxghDwsa9s9iE2Yfz2098Lq7yl4nqQmo0YXSF-zydWg6_RU18ty5upx4TpUhRII2gDpfwxGMgVGiEW_uKLDBdIWMqq9DJrWUk2pJjcbV6w47UFeSVbzCYaX7SR6A4C2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=nDs4pOpxkIVMIKvkfs_ICj6jEjnTabhNDZMAgo15LruxiNzlzqXseok3V7ELRYjVprq-s1Bow_ynouYjC97s7xXXjPdRJnAkHtAOrieGq5sS7_UZ6tT0MrxG6ov922eRxaAHiBlO4Klkz32F9vcFzMR0cLzYf9j-tmGWFTU1STBqPf-mPLYKDH2ZjNBphDR7AfLMqk16bRAbf1akvXqBHnbxghDwsa9s9iE2Yfz2098Lq7yl4nqQmo0YXSF-zydWg6_RU18ty5upx4TpUhRII2gDpfwxGMgVGiEW_uKLDBdIWMqq9DJrWUk2pJjcbV6w47UFeSVbzCYaX7SR6A4C2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=IpiNUpmaaDNGpBH-iCsSo_tqkeKXg0YOdTIzpuMqL4dhfVkgqAMeODQXN1CufMYy_cJXMPdk7bfq7IWEZ8ozqxK6Nw-ByoZKIOBVQqpLZWzx9Z_31XfJfnNd7S9JKTFI7L3zESTNlUt2oJ_vgjha0hhZ1kC53cJ95ZoBtfVHKCDoYSgWmaueOl0b2_AGceQTpVGh-XyKoJb8iiG-VwHgtblSF5XQ3NvM-IY13WMJZq8C-XhVJl7IJ8HhE_xWMlnOOSrZK2ctEgb3VKyvwjP-nSbYiNBwoG2fgYh1ha7x3brukRAyTp7ahUphLkROxoOm_Y4_nTh5nry0HEU1g8lkqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=IpiNUpmaaDNGpBH-iCsSo_tqkeKXg0YOdTIzpuMqL4dhfVkgqAMeODQXN1CufMYy_cJXMPdk7bfq7IWEZ8ozqxK6Nw-ByoZKIOBVQqpLZWzx9Z_31XfJfnNd7S9JKTFI7L3zESTNlUt2oJ_vgjha0hhZ1kC53cJ95ZoBtfVHKCDoYSgWmaueOl0b2_AGceQTpVGh-XyKoJb8iiG-VwHgtblSF5XQ3NvM-IY13WMJZq8C-XhVJl7IJ8HhE_xWMlnOOSrZK2ctEgb3VKyvwjP-nSbYiNBwoG2fgYh1ha7x3brukRAyTp7ahUphLkROxoOm_Y4_nTh5nry0HEU1g8lkqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=KHVQffMn9RvTZcRUtt3sBh4FbgmrdetV_JjDi-Eb3a06Zxonh-sEkvmwac73H2SNQnCypfGUOT5PORiHO26mY7ozRmz2FndAWOzCQ4P-eUU1-FE1KEbLUsWa6soZhhBDQONuRwxjaprdMt9poyCgQyiyYbCntYsu5laOynvb7xKjOLMy_FbycymkPUa4tBtaAu7eKdF6B-lRV5GG66mW0wXn-Xurf6Qnk0QN-frOWYoNhSLissy2KvqFIbAGQUaAWHooPkmd0SX8lyqipvOMQpRMskLKVi1VYCGTtzCllizCdicna4c7BrUkgAe5swBEdwoCxd79dVEEG6KBw_x25Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=KHVQffMn9RvTZcRUtt3sBh4FbgmrdetV_JjDi-Eb3a06Zxonh-sEkvmwac73H2SNQnCypfGUOT5PORiHO26mY7ozRmz2FndAWOzCQ4P-eUU1-FE1KEbLUsWa6soZhhBDQONuRwxjaprdMt9poyCgQyiyYbCntYsu5laOynvb7xKjOLMy_FbycymkPUa4tBtaAu7eKdF6B-lRV5GG66mW0wXn-Xurf6Qnk0QN-frOWYoNhSLissy2KvqFIbAGQUaAWHooPkmd0SX8lyqipvOMQpRMskLKVi1VYCGTtzCllizCdicna4c7BrUkgAe5swBEdwoCxd79dVEEG6KBw_x25Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=CS-TpBn8medneBQfwETGjhlF4B26PYVxxYpwDodPCLBlutYuBUiKPU75QE8XezaoypaM8Sejr5kRPWCEqx38b9vD9oZ5BFpkCpKZVnMwk5BAVrwKTD2Op_oJO7OoAZGC19TVAiIo0dgLeEyGG0pMEinfI2sRQqgucKZKbWuQ3DSMRg0qKYJYIfvjjem-S5338l9AEgSkBrGd7iOVXvRZf7qrLGrRMNa_Gk2Wxr3-fVD0JSlB-CiXR65cBrRjQitPL8BiF8JdaWFAKx-JEfX-UxGSX2ah3qYdIFy7Lkogjibjd53AB1vvTRH5Sah7xQwmzroJCDKZ6S9mJaMsHTdGJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=CS-TpBn8medneBQfwETGjhlF4B26PYVxxYpwDodPCLBlutYuBUiKPU75QE8XezaoypaM8Sejr5kRPWCEqx38b9vD9oZ5BFpkCpKZVnMwk5BAVrwKTD2Op_oJO7OoAZGC19TVAiIo0dgLeEyGG0pMEinfI2sRQqgucKZKbWuQ3DSMRg0qKYJYIfvjjem-S5338l9AEgSkBrGd7iOVXvRZf7qrLGrRMNa_Gk2Wxr3-fVD0JSlB-CiXR65cBrRjQitPL8BiF8JdaWFAKx-JEfX-UxGSX2ah3qYdIFy7Lkogjibjd53AB1vvTRH5Sah7xQwmzroJCDKZ6S9mJaMsHTdGJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=Y1RzjhyOJDLWL8VC0RfbDJ3Nzi6v2fSMqrITFqbSAQBmD4d2dN4I-zURmae-5CXkFFQ-uB7pQxNhC-lgwz6kvvOyymrBzgqBj5ctvHE0OhWaQi_Dg-GaGvurWI2z8f8DqcxVteeV49L23p2mlmeIv17Ue5zpYwCEzeXNzheYfDK6S9HmVHmPRSmEhEM6AkLhyC902uwsoeD3-GdvlnznhrBisQHiH0iV79QJK9ITJPDiR40FuOMS_E_30y0NBxrOjy0yDkE_0vQCObT_qRoS5Sg-QtDk_MKxfXwXPtPDytLoGQag2l9eSNLWARg8h-8oxvNbfK815Er-pl-q0uj1sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=Y1RzjhyOJDLWL8VC0RfbDJ3Nzi6v2fSMqrITFqbSAQBmD4d2dN4I-zURmae-5CXkFFQ-uB7pQxNhC-lgwz6kvvOyymrBzgqBj5ctvHE0OhWaQi_Dg-GaGvurWI2z8f8DqcxVteeV49L23p2mlmeIv17Ue5zpYwCEzeXNzheYfDK6S9HmVHmPRSmEhEM6AkLhyC902uwsoeD3-GdvlnznhrBisQHiH0iV79QJK9ITJPDiR40FuOMS_E_30y0NBxrOjy0yDkE_0vQCObT_qRoS5Sg-QtDk_MKxfXwXPtPDytLoGQag2l9eSNLWARg8h-8oxvNbfK815Er-pl-q0uj1sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj-JJKygULHJ6I0Ql_XW8Cn169BlX5-pyIHf6IjbTAwpjbPEzBkvWyBUglt_eMjk8X1vln_loI_giT8aMR7XG75YERLSl8hniyd1n5XlZneAX_RhtazDF0dhzcBIB-OSiR0EWevlV8FRGjPMgwQjknH1hR-Kwr18peFdAzUoTBeEp7HEqgYqaIO76S4WGr0ynorgl7CG4wCjai5e3lnCbRqr5QQFxeB6VxT_bXwTch1ZBFHIRQ_Ze3XgbJ0eaIXatH0RSY61Zg_xdh0zhUbaHN_tZYDOc7BH4avduJm3l5-LglqyDF-o9Jo3XvGMpgqSiAVzD_hWtbp96nk12jUy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=eXlIkK9OCQ6W7-a8A5fOv_Zk56E5PMHCbv9Py8x7RKv0iGGtqI0bLGUxwzHFSOb1084QxAJNvRjnnbovvqeN76horpp11kbApsaR4htqXzPSFnCsWc3h9qISC0Ay31A7C1A8WjFJz8sfI7cs-ZHRIoR1k8RV0chETfBOyGaobvjfkKbxohwr_PpRmAVXf-GFs39KMdJ0g8zl9cpJnnyCPetAWIwmJElSp3N7iX8wLkAz2byUYmtnuvk70fEKnYXp-8Hc7Ppl5qAuEeswLate2SPGSyvZsGVkKL54v7qUy7OE28wK6_4LkG2KhmdFafiRv2rDxmstOSh8gqhA6RsdJYTwC0110QySH7f8wuTnneEKH7SxCMkIjMnOgZ7Qw7guNjoEowqLCUCvdFQHrzRquF9WdM3aSzDDnFElMZxAHBUgOwcGoxg9Mmaqwv0PERy8Pe7uCEEKzz2qq9rxxWeWFRreJWJdbi80SrLIyfs2TjfRdQ-P3E3NtQyaRJgup5GyVWFI51q8uOPUXO3Mlf6dNHPBMtwX1DfrxbCzwUhwjfgpmRUVVhcqo17Qe13CR87y1zKLkD6YlTqTjhnkBP5KvqxIu8WLKi6tkKHYt4NUiDfWUj_7PAzlPHkzWPjwt3ELOXrGf_ApeCBz8OetHP-ipwiCpaQjCuFlljNV24uon7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=eXlIkK9OCQ6W7-a8A5fOv_Zk56E5PMHCbv9Py8x7RKv0iGGtqI0bLGUxwzHFSOb1084QxAJNvRjnnbovvqeN76horpp11kbApsaR4htqXzPSFnCsWc3h9qISC0Ay31A7C1A8WjFJz8sfI7cs-ZHRIoR1k8RV0chETfBOyGaobvjfkKbxohwr_PpRmAVXf-GFs39KMdJ0g8zl9cpJnnyCPetAWIwmJElSp3N7iX8wLkAz2byUYmtnuvk70fEKnYXp-8Hc7Ppl5qAuEeswLate2SPGSyvZsGVkKL54v7qUy7OE28wK6_4LkG2KhmdFafiRv2rDxmstOSh8gqhA6RsdJYTwC0110QySH7f8wuTnneEKH7SxCMkIjMnOgZ7Qw7guNjoEowqLCUCvdFQHrzRquF9WdM3aSzDDnFElMZxAHBUgOwcGoxg9Mmaqwv0PERy8Pe7uCEEKzz2qq9rxxWeWFRreJWJdbi80SrLIyfs2TjfRdQ-P3E3NtQyaRJgup5GyVWFI51q8uOPUXO3Mlf6dNHPBMtwX1DfrxbCzwUhwjfgpmRUVVhcqo17Qe13CR87y1zKLkD6YlTqTjhnkBP5KvqxIu8WLKi6tkKHYt4NUiDfWUj_7PAzlPHkzWPjwt3ELOXrGf_ApeCBz8OetHP-ipwiCpaQjCuFlljNV24uon7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=h2FbK6nG08vvOnAWaDMGPIAWZ4HITnQfSXUaTTUgoV02sqdPwVroe30Cq5aOYYRFt_Py3r1F9sg2YJ5fwOj4N-c5PLJdbRml54-h4RbOtqe5aCl9V6-WCncX7PJfBVSPDSHlSJKPvq5D2BfDhiIUXD_Y3OOMrfsHon4ms8zM8n7r2QpNfC6b0gum31TjqYHnJLoFXYwilRkf9tgxs-HcUxP-o_bfMG9U5d30kBXq4Xjd5MELNTJrXja36lhKf9cY27uf4O9Ogg0BBAnZx4hc1bA8y05fJO-CsToc3oMghTTK_yPRjyYIpeSnLfIHIPV7KOSFQOPKqkRDxhY4HChshQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=h2FbK6nG08vvOnAWaDMGPIAWZ4HITnQfSXUaTTUgoV02sqdPwVroe30Cq5aOYYRFt_Py3r1F9sg2YJ5fwOj4N-c5PLJdbRml54-h4RbOtqe5aCl9V6-WCncX7PJfBVSPDSHlSJKPvq5D2BfDhiIUXD_Y3OOMrfsHon4ms8zM8n7r2QpNfC6b0gum31TjqYHnJLoFXYwilRkf9tgxs-HcUxP-o_bfMG9U5d30kBXq4Xjd5MELNTJrXja36lhKf9cY27uf4O9Ogg0BBAnZx4hc1bA8y05fJO-CsToc3oMghTTK_yPRjyYIpeSnLfIHIPV7KOSFQOPKqkRDxhY4HChshQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=nmpv0mGhwks3fDtLY4u_OD1oxk4bnim_1pXtRvrsnyBuFnZKTj5w66SBiABlUpZJG1hBzlja2DeSneIOjPrnXVsmagFy51F-8rjJgVPvaJgA4zp7JbE1Bl-IEYt_b4cHd4R5-sYSNymR26RwvwLCMXISixowVBSgQ2eohx_6HfifqJD_4b7gKsiFiTh6CSF4m_UB8P-HyPnVZ9ISz9oxgihdkqYw-4IbiPn207aGrSj8C4eOrD_QPQgpEubDhBtC97REX5z46xmp5YEuz031Ao-L_YwE60-ZQvdVZMxVthbbogULRTD2hmSwrECvJLoYF8ybn99I2fPAao7hIDCI3X3Dgey_DDk3tuJfx7-CyxGTiZaS-FhVzbXoZIbvlJ_jneQdK5Lkdx92fyZyWhbVsH_Fqjty5qy4N4oat9irZHAQa8hMIn227FJbiKjZOJPNd2bhBdg35KDpLSgLBFb8scjCUWGdskktB3cGMMfKlUnrw0IxkZvzMW8zW3GQMoshG8-jvyT0kCUJVfJIlHhtl0pKpBungqOCWRRqTFbIymCNkdU_APNnDBH3TdhQnp4AY95CCOUEPpYJB3hDwiOh0TH_MYVFNGf1JkNH2fwNdz96qy2JjNJ6y0KhEKzqV6OmqOGEP1jwqdajMUZltlVc1pomgmK9QgZ3pgEk6-35Itw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=nmpv0mGhwks3fDtLY4u_OD1oxk4bnim_1pXtRvrsnyBuFnZKTj5w66SBiABlUpZJG1hBzlja2DeSneIOjPrnXVsmagFy51F-8rjJgVPvaJgA4zp7JbE1Bl-IEYt_b4cHd4R5-sYSNymR26RwvwLCMXISixowVBSgQ2eohx_6HfifqJD_4b7gKsiFiTh6CSF4m_UB8P-HyPnVZ9ISz9oxgihdkqYw-4IbiPn207aGrSj8C4eOrD_QPQgpEubDhBtC97REX5z46xmp5YEuz031Ao-L_YwE60-ZQvdVZMxVthbbogULRTD2hmSwrECvJLoYF8ybn99I2fPAao7hIDCI3X3Dgey_DDk3tuJfx7-CyxGTiZaS-FhVzbXoZIbvlJ_jneQdK5Lkdx92fyZyWhbVsH_Fqjty5qy4N4oat9irZHAQa8hMIn227FJbiKjZOJPNd2bhBdg35KDpLSgLBFb8scjCUWGdskktB3cGMMfKlUnrw0IxkZvzMW8zW3GQMoshG8-jvyT0kCUJVfJIlHhtl0pKpBungqOCWRRqTFbIymCNkdU_APNnDBH3TdhQnp4AY95CCOUEPpYJB3hDwiOh0TH_MYVFNGf1JkNH2fwNdz96qy2JjNJ6y0KhEKzqV6OmqOGEP1jwqdajMUZltlVc1pomgmK9QgZ3pgEk6-35Itw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=hqeIqLsBCBG1i0GWOMKmL7WyKEVm7p4nbpUc31M8TJglM8dL6nuHy53QDeempqDgcYCgVk3NepEKMRpo1xfdUqigmXPpLhpGotObtq6y9R274W5D3sqDdFHEeygt7KkSEIUZm7AS2SmlgKY7XKl3p8ZQARBwqD5UE3DWE_eeiOO8hLVE1UD-MmTkv717TiiW_BPtSbOiETQ5x8hyRyl8xt9w7O0Sj-2pzxucjixmo5LifaIFYoqOKtl1s2bzzj3f1xswJ3aN9HdSt-LueoDfEv8qXc3Qs4SYWBBBtcWspFJo4hake3hKZqh0lg42TanTjtNtiDvRg1t3fI0LbSTy5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=hqeIqLsBCBG1i0GWOMKmL7WyKEVm7p4nbpUc31M8TJglM8dL6nuHy53QDeempqDgcYCgVk3NepEKMRpo1xfdUqigmXPpLhpGotObtq6y9R274W5D3sqDdFHEeygt7KkSEIUZm7AS2SmlgKY7XKl3p8ZQARBwqD5UE3DWE_eeiOO8hLVE1UD-MmTkv717TiiW_BPtSbOiETQ5x8hyRyl8xt9w7O0Sj-2pzxucjixmo5LifaIFYoqOKtl1s2bzzj3f1xswJ3aN9HdSt-LueoDfEv8qXc3Qs4SYWBBBtcWspFJo4hake3hKZqh0lg42TanTjtNtiDvRg1t3fI0LbSTy5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=B47XWhE8QH_Rd-qtC3j8Yo7xH3hCH02XslG7KSa4xgJp4-rnu0oAX47a9wRlJJwNbLHGlr7xGJgtbqzXRF_kyv1loEsA_MML9vC273BZp82htVutMXEGZ9VdaPYEncyVtnOdqX_k0oihMC818Oiy2VDftN6fmviNDVy-ukwxcTlSvTnXRRbQ0cKDXJaJ0d7qBZKfn4zDBlGdtrvOPlb6UaffvWfn2rdBHiJOZmM8d42n_bauX6pwmD40Xm10HwAmwZjXZ5jVAb4BAN0GR4wNkqrREQfpkmT5FzLap07beqPlIOg2akmAa0yzHwznU2vx9hJLDOLrTpY--5eIEZMEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=B47XWhE8QH_Rd-qtC3j8Yo7xH3hCH02XslG7KSa4xgJp4-rnu0oAX47a9wRlJJwNbLHGlr7xGJgtbqzXRF_kyv1loEsA_MML9vC273BZp82htVutMXEGZ9VdaPYEncyVtnOdqX_k0oihMC818Oiy2VDftN6fmviNDVy-ukwxcTlSvTnXRRbQ0cKDXJaJ0d7qBZKfn4zDBlGdtrvOPlb6UaffvWfn2rdBHiJOZmM8d42n_bauX6pwmD40Xm10HwAmwZjXZ5jVAb4BAN0GR4wNkqrREQfpkmT5FzLap07beqPlIOg2akmAa0yzHwznU2vx9hJLDOLrTpY--5eIEZMEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=R10mHJ2ON-6b9Ul86vJ-Q2wc4hUHaF-AvtgwQagn27OVBNz0KZvv87335JcMmA_OrBUf_29PikGdHRfz-ilQeD0S1y2xIjAS4qTKR9SZdWlUeybi_lq05C-bZ8MHVdQuikPcNOKoRtWw8h1Nym0HNPgBQqjPdv2L73LPOrhOyvvQ3NBN9JgY_k968gJ90BpEV0CM7a0G6xMj_6JzdYKwgV5VPjhM-MLdTbkeglZ8UbinXIda-jAIranYxEAmxIng6R2wajpowoh-LQQdNP8mMV78OI_PklLnI6oDsMap1OKF9mb4tRNyy5E5F3nV-lEN6Ozb6TSxiSN7sTdcif8kfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=R10mHJ2ON-6b9Ul86vJ-Q2wc4hUHaF-AvtgwQagn27OVBNz0KZvv87335JcMmA_OrBUf_29PikGdHRfz-ilQeD0S1y2xIjAS4qTKR9SZdWlUeybi_lq05C-bZ8MHVdQuikPcNOKoRtWw8h1Nym0HNPgBQqjPdv2L73LPOrhOyvvQ3NBN9JgY_k968gJ90BpEV0CM7a0G6xMj_6JzdYKwgV5VPjhM-MLdTbkeglZ8UbinXIda-jAIranYxEAmxIng6R2wajpowoh-LQQdNP8mMV78OI_PklLnI6oDsMap1OKF9mb4tRNyy5E5F3nV-lEN6Ozb6TSxiSN7sTdcif8kfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WblRXmqBq7P61pLnwp_X3et94bW7JgePaMBqAR-PNDMCFwNhxOh5E-7ecdEZHEQjjnNLQzHXc1CeCNdIKAgpUfAkjxlJhScyIoHkLJvwPXBgsjUCY718PFsXCDnigzEYei9GRtYj0qj_qT4BEWoJKhnfvFESiNVk7Kf_vBt6RHuaAjCbGqrkIZkLqVrRq2VTPo_UT2zLj6hGdfWG58VgO4LNj-Bvl9Qb1G0HbA4mEL1YfARnXWL-YTHLlmjV6uI_pm2FH3AeWFEC3Gt4U52wUOW5LrPCMA3J02fOmsxsyVYNu2sFzCRrZZa9D1udQ5ZZupreuZM--2YA5TTYZjZ5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wjgp3TxuhGECx0CHcLUsgeNmsnk2aaB0_yvIjgTA1DDC6Suz1G4i8j5BIelxM-pqfFzZzQ6vU59Ynl6vbTMdTPwv8lzpl1ac3Zj6haLmDvjAc-EejUY_9-_GgU72_I9ng-vxo_B-L3JDwRVEnABwUbMpo4_g3LohVsfWUw7HHl1rLcqIycfpIUGy0FAWH9OA3qAHbUe0cnDT9rQCmJq0wyo413EzP6qSjQe6lu6czlTi9cpnYZCDF6U88_SJhH30Bfww_9Ti96FhO6R60Z6weVMBSGU13pLOj17ib12OaGBlE0eJlifikZATkhPuS4hYA5DA760xAk0c5uthRlfAAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWkWubBxljQUvccwyapGjPoLsZldfhfmR7WeSFCvj3IyQ6JyRKgr1uIZXwUIfrz1UgLMDC8UdFVOEnAKMaehZeIXDLoxQ7lTrvj3eoK1YZf_LDbSscF_qcsl26gZ4mniKhvGC01r5krNlWxmO1cQgF-gyJFiSQIxSAPDBaxp892lM-ouNmovwpxpvyJiaX9dNFbd0hqMDdt0ElFQ9St6XUmF3lwRj03DgDRAB86-u38VQVBJXb2JviQSgf5Mu3aZG6riD7tpcsxy5aVOAB36GO7_sXERgfRF9VwYQH2H3vebVi0VJ49FuEU4IQFH1FG9pCZqJiunhhe6Z1pnRSG2BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrNrcGXfoE26_w0qy_KWadDtL3IsQjsJRypSApbUxZKYvpG5I8ZXyCl2d9G5m7nrfpct4Nhz94S9EAcIQyTlfNO0ULqMgca8qd-xrfbsJOkbgHDfc3NIus0WLrivXPdFQ71CzbjtHkYpcR-2JiEkRQcZnLIBh6ATeH9B98nV_fIcEgWUfhVj4TzmhlF6HduadVIK-2O3AFnORFSGW37wU8zeyy6vsCcNPiv1u1NM5KpcAjJjiPQRETHTObulxxitS1u9Etz2IXr5m-dixsO_XqvTfv3s1k6efJhSHxvTpHYI58U0qLwgigBkHpJ6l66MaT7-yZkm5lfPwmHrn2HNRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSfjePJXjNLnTiaFdelAnGvbXurCPMBlfOvx5lk0cTYaMHbleMNwanE1vNx8hieyCGpT9joTK5JxdyOhOcgO3pDJCNRhMlmv3LMUVzGlt9abqiy5eUxqzGyI9-BscmoD1ebn4ic9fcYJRtQzTZp6lsqsF6ssUQKJG54E1k2NYS0x3yn5a9b18uISWa6N-rVNst8DPyNAXOeWmAAaThdg64QPourCnT6I3wKIDwCxZbWbkEu9ABjpFocn_HHwB3JwIUr_bCvXE8gnISVjSDXuSibBbI4aq8N8W8znjcdYo8D0DXf-TwWkG9L-wwAQHQOBTclJ3Nt1FVDeyMLq7kfXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzvNKrYOm9f3NbUw7shrZtFR34D5dkYKHM3Mg8gn2k-a2K0lNZLcrjZOx2yNiZXEZWytAsLCSMjZDSn3csK-03mGgvXvTznZyq_HqqC6N7U9FABKxM7slUif0BOJFjtULg73Ns5ODo84tuHOkOa9FZjuJcBYfWrK6jN6xTRxE9c2dnBSbmb_yClG7D-ep-zceVdAAnWx8pP_xKa38kDp61Po_303WLAN9iIiz9-OiUD_3uhqBl_zaasmbJULSOTaL6AKBW-yrn1JbM6n2UovnAKCLbRvhTrQLBSqXLB6bd2K7ukn57RJVAVhalGM-Sr-kymKiF48BmyRF4blLNryeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=EdPJgcOe9NTt9DP9Kz4nS5MG21EvDiBK_jB8B-zpniJHmkzUqBk0Ex7Z-ak6dcFricGnKCxhmXH2wWY03w-loJ0Qxrn0zAGrb3vgedAz3F8zUiNVCJCmy9LB3LGJ8kmcSEl_7RWpPQCbxTjAh4q8TiXg2BqzIecHVMmVPD-ELq-46SmnuVD012qlOl0bcOtd7gDHcuaptHzaWulxA5hdVy8pzSs9eRtXK6hm4rlDzKtodcyfQEj0V6CHC2Zxdl0T2ao0SglCGf-RnrAonR7SJ2f3cLwSzRdosfU3_OrKPSmPp5JfO2V5musqVJicgWF49MJb-DRoDhMSI8sLiHpx_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=EdPJgcOe9NTt9DP9Kz4nS5MG21EvDiBK_jB8B-zpniJHmkzUqBk0Ex7Z-ak6dcFricGnKCxhmXH2wWY03w-loJ0Qxrn0zAGrb3vgedAz3F8zUiNVCJCmy9LB3LGJ8kmcSEl_7RWpPQCbxTjAh4q8TiXg2BqzIecHVMmVPD-ELq-46SmnuVD012qlOl0bcOtd7gDHcuaptHzaWulxA5hdVy8pzSs9eRtXK6hm4rlDzKtodcyfQEj0V6CHC2Zxdl0T2ao0SglCGf-RnrAonR7SJ2f3cLwSzRdosfU3_OrKPSmPp5JfO2V5musqVJicgWF49MJb-DRoDhMSI8sLiHpx_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=s4QLtWCcuMAvaNW_kbvFjmJeAPXssQVW-9y9fc1KPtka3F0eE3KuWsw152yUwDckVmZOzwgaelOjs9WJV30gZheJF81_k76DJ9uaw55IB4CRh_YB2FYuIZCWKR1GTKsWwl3pvfYE9922OaBA6r4Mp9ebcMzPXBpczwNuZu2eYs9_q0jS43tLl0Cm8Fv6JLcYt6jgJOroBi281Fedg8cdLLIZLFKzik8I3SB2SD2tyM5qcBvSAp8HEEf4EgZFDxAcDTTXKM71ZU9-oYMDEXOlLGRjw6YuX_ivWDeAhrVXFouIJZzdXcLI-t9gr5fh3HeuNiZz9z8vjOXoflW4pT8_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=s4QLtWCcuMAvaNW_kbvFjmJeAPXssQVW-9y9fc1KPtka3F0eE3KuWsw152yUwDckVmZOzwgaelOjs9WJV30gZheJF81_k76DJ9uaw55IB4CRh_YB2FYuIZCWKR1GTKsWwl3pvfYE9922OaBA6r4Mp9ebcMzPXBpczwNuZu2eYs9_q0jS43tLl0Cm8Fv6JLcYt6jgJOroBi281Fedg8cdLLIZLFKzik8I3SB2SD2tyM5qcBvSAp8HEEf4EgZFDxAcDTTXKM71ZU9-oYMDEXOlLGRjw6YuX_ivWDeAhrVXFouIJZzdXcLI-t9gr5fh3HeuNiZz9z8vjOXoflW4pT8_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWfzDaUBXjUq9hZhLd9lN2zEr0EG6T1Lj6uiU9UP-d1qrinz1k9lAp5WOCmea_uMahFQVZXKv8L7WbMnufwHLtGVo8iv6s-Cv2dlyU4vlZZvExw0iWA14GaU-sB8zGHLuJXkIVdLIuhGvd1zTKKXWOeQxQ4jOBWy9Hy43dnPwH7BhLsBZG_z1sSsUU7S378pcYtrUtgtB-JNBWTHTf1iCsvzBpMyV81PHo4cYhfGqAF66glEV9XOXhrROPU8KsFuP_js8NyAhcvBkl7lDEDijj98Yg_bBazoIvsn6OuzgO3nx6yPEQgtF-O73ga5m9x1AgxbvQqkQwzMQRk6ubnWYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ldmk2sFpIc376-tJ7CAkq0ou5u3ux_VayXUd84SyNFd-_KlSk3gDs51OAC3s5wwOHFkCV3B2rc6NWKftwbVgtbD4IIz7y6AynBCxNHfvQdCm3AiN-7Eprass5_h8LtJhSvDRAwNH3Ro5r2aq2pculgwVO8A2oOE6Y1RYryay7EXT7tCBolrmMFoIobutGlADQ5Tr_m3nuj827aOFn5diLsn79nm_IbTVF7XVDOjEpWjJfchYoqZWG5wDO1XOVZsy__nUsM_QqHc3ew5QpxkcxYHPAU1CgkngOIg5RaCSDIMSiQcCrjFflJAuCYsTYtaAWorkOVnkp42Lol4vAuiTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=IcX62F6KHeFfCIRAl_nfI2nQBLyjZyiVMcAc2F4FTQf0pZJn5sQWF1HPDVBnkJmqD8b5oLNAFFbItjndh4pM2ikouMb5fwzJkfLG5tJZdKNYJ9K0151qIA9FJZKkV3sifxvG_K7F8FAExFcMMAjPCLNujzLa1O2YK6PjxVEuy2DdPvAvebGHBxNSErqY0JRiaqv2x5PWrqmgOUvep3_vAg2OynurSMdelB0J70kHTxTtk37z5Jtw_LiaRULKaYIUAsPLZQFMaD0TwMCA1E9-Bm37D6xVeRqoMltx452FdR88aErJcAlTH11s6eMCgHGJoKz5duLb-qtxsrEmHd5Dpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=IcX62F6KHeFfCIRAl_nfI2nQBLyjZyiVMcAc2F4FTQf0pZJn5sQWF1HPDVBnkJmqD8b5oLNAFFbItjndh4pM2ikouMb5fwzJkfLG5tJZdKNYJ9K0151qIA9FJZKkV3sifxvG_K7F8FAExFcMMAjPCLNujzLa1O2YK6PjxVEuy2DdPvAvebGHBxNSErqY0JRiaqv2x5PWrqmgOUvep3_vAg2OynurSMdelB0J70kHTxTtk37z5Jtw_LiaRULKaYIUAsPLZQFMaD0TwMCA1E9-Bm37D6xVeRqoMltx452FdR88aErJcAlTH11s6eMCgHGJoKz5duLb-qtxsrEmHd5Dpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=HTtmjya97mrVtQszbKZ66Bz2EczdiFN4eLiq3Agi9Xa3tT236ozKnFVf-LKCWIXn14t8lfAIiMuntSWtfLgxictbh_U0DmbWEUxNtIGTtQBR5XprYSg68BeAZslFYdVVWkiV9JwVCjsEzQDpXNWfPCFhLZ93Q1L-fMqfGGYvbTIMibDGtcc09iY19URm-vpWyWndm3ZQQ2dDBsJl5gAj_xPq-OlY6FL36mFYds7HnAMozgzttGOuv-qFqPzJ4Nad6e0cgEVM9d7KEu4WqSwXrGhK9R_SlPhj5WXJBP-mCxXNcSEK2MqyNgw_RpYSK94SNxkYaxV9vOO72plLqp6HMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=HTtmjya97mrVtQszbKZ66Bz2EczdiFN4eLiq3Agi9Xa3tT236ozKnFVf-LKCWIXn14t8lfAIiMuntSWtfLgxictbh_U0DmbWEUxNtIGTtQBR5XprYSg68BeAZslFYdVVWkiV9JwVCjsEzQDpXNWfPCFhLZ93Q1L-fMqfGGYvbTIMibDGtcc09iY19URm-vpWyWndm3ZQQ2dDBsJl5gAj_xPq-OlY6FL36mFYds7HnAMozgzttGOuv-qFqPzJ4Nad6e0cgEVM9d7KEu4WqSwXrGhK9R_SlPhj5WXJBP-mCxXNcSEK2MqyNgw_RpYSK94SNxkYaxV9vOO72plLqp6HMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=TofTwirP1vuo8J3ZWADmhRS-APY99N6km_7JAGC2gLsnug6GO1o6Ta8lj5x49QTwJ_bLWcKuKyFQOTbu20wpKb3JJbo7wpwsFEiZ12cSXW3gvN9d2YFRHkwrZ_GpwGWBPxgT5-vfEm2-F8YOtUCLwgGdIL2Rh2TlZjqvGFD_TI9tdWLwwt7CpEAF8eg5BcibHMNpoY27QTqZEEmMgcpim4xsQAt_I0Xazsp2lMObI_rlwRLagxrLymjftLvGwQuiiHY3QoNq6ujF6-dvTaUgitpZkGQoitF7RVNSFHEVGRZNIiuPF-oDQw57xyrztTM_EeXViy2Nv2XrNwpCD-iCfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=TofTwirP1vuo8J3ZWADmhRS-APY99N6km_7JAGC2gLsnug6GO1o6Ta8lj5x49QTwJ_bLWcKuKyFQOTbu20wpKb3JJbo7wpwsFEiZ12cSXW3gvN9d2YFRHkwrZ_GpwGWBPxgT5-vfEm2-F8YOtUCLwgGdIL2Rh2TlZjqvGFD_TI9tdWLwwt7CpEAF8eg5BcibHMNpoY27QTqZEEmMgcpim4xsQAt_I0Xazsp2lMObI_rlwRLagxrLymjftLvGwQuiiHY3QoNq6ujF6-dvTaUgitpZkGQoitF7RVNSFHEVGRZNIiuPF-oDQw57xyrztTM_EeXViy2Nv2XrNwpCD-iCfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=vX7K2nl8PCXVBMClsew1l0zXpGrI8idF0kUMn94jGL7Umx5sMnTe4VoT9RkoDhQg02YZPGSnn2B2qDAB-Bg_KZnJ2eDsgbRM9j1LeL2ug5isWkHyef9DjT2YhSiO2o51Liq88_U-YNxXkfzvoBqKkKJK2-NNbCLQfq5dMMcaGQOJpM8oN5uqTm5KlZDHpJ5YgdDcgfxqMT4jsaVcKzOOXcT3YQqfNuwlQGi0x918XGMCB-6yiIt8xIhhOBxiVc2_GObjmoHi-PpdEgjMjGdulvou_L_TPls_ugYU3Ba9krnd36EMUKk8hGz1lv-JBA5uS35sOivcIQGiQm-RFMWewGmafEeal5K47qz_v6dzwwEBAHGT7044_REdN0qH84OqX3v7RGnncZH1ZyAVQOv3zT0AyGrqn-8iUBjpxLcAtFKuJyKhR4T7ngAo3k8UKdD0OH8EKvo0lTBSsAGG175Eco-njPTrcazU7gvt3JObwbOM73sLhGu6pMvtYIC55bZ5Kfo7k4TAvFOgbm9L7I1F9i2g-bHuO93j9NYCZwBAaTwRb-apuDEDe4efMWg3I3pHYzeZbc56q2c0hDrS81B7gN7JgEs70Zwtsh3bO9ZP15lWiUuZK4x3qDXY0C9Nnipg03LG4UwrHnDv0NI-TLPJTdrsFBIBb2hki5-Zbr1PP-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=vX7K2nl8PCXVBMClsew1l0zXpGrI8idF0kUMn94jGL7Umx5sMnTe4VoT9RkoDhQg02YZPGSnn2B2qDAB-Bg_KZnJ2eDsgbRM9j1LeL2ug5isWkHyef9DjT2YhSiO2o51Liq88_U-YNxXkfzvoBqKkKJK2-NNbCLQfq5dMMcaGQOJpM8oN5uqTm5KlZDHpJ5YgdDcgfxqMT4jsaVcKzOOXcT3YQqfNuwlQGi0x918XGMCB-6yiIt8xIhhOBxiVc2_GObjmoHi-PpdEgjMjGdulvou_L_TPls_ugYU3Ba9krnd36EMUKk8hGz1lv-JBA5uS35sOivcIQGiQm-RFMWewGmafEeal5K47qz_v6dzwwEBAHGT7044_REdN0qH84OqX3v7RGnncZH1ZyAVQOv3zT0AyGrqn-8iUBjpxLcAtFKuJyKhR4T7ngAo3k8UKdD0OH8EKvo0lTBSsAGG175Eco-njPTrcazU7gvt3JObwbOM73sLhGu6pMvtYIC55bZ5Kfo7k4TAvFOgbm9L7I1F9i2g-bHuO93j9NYCZwBAaTwRb-apuDEDe4efMWg3I3pHYzeZbc56q2c0hDrS81B7gN7JgEs70Zwtsh3bO9ZP15lWiUuZK4x3qDXY0C9Nnipg03LG4UwrHnDv0NI-TLPJTdrsFBIBb2hki5-Zbr1PP-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=M6pLniHWYPcShWVUZHX_2Ip8u6LGRm7EbuhRsxDzW_e-AaEXu2JWTauMBb86BtlCPBQJguLIFcBWJUvrYMx-M10VHLnIufW5SEOYnN7jx_HwNPyL9FSOsLlN9JHx0YiyX59VccThOtY9o1Wd8guRBCcAGAU_DJBWWIpzQc9D6jVBBPgAZtf3YLjcTK1g5ExsFs4e_NlXoxED5TBoMMGfzxdUp08IzBbS32fycAzavNyuv7T95ZspD1KFYyo0A_LzW7lR4LFXoQnNSWHmuDTPyWLQvYKVFNiK21HWwBOAS1yMLM4-eZhLBMpGpXXj7UgyXrgvVkCqL1CzxohkoqoDX43qrFL80xLz3wOUevdfWopRFm4Cz1BaYkeXdRJzzaCkuBz1ynbNEu618bbxAX-v2CjNj2b3H_Cjuduf3GqyvlvId9llcHe0O7hj4Il9amI1TlXNNnIkj2kwG-lPWnVkOr1R2LcieNFx2zbwEIx8ALraqNW-4KvQX72IJuYZQG5ZXy2Q7_PqMYJRMAcJaigPtw2qM3lAUFi-X_xBR6bydqwrKl_gXWanm3qXMCpoUrv98a1gX7yFzBvCczYC9-zTSFm4uFvX49CtM5_j6_6a-FYiAC3vwREmydA7dCJmSCi8zk-nL43uvZeknZW-Nf663xXQOl90hNNDXSDTw6NbRok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=M6pLniHWYPcShWVUZHX_2Ip8u6LGRm7EbuhRsxDzW_e-AaEXu2JWTauMBb86BtlCPBQJguLIFcBWJUvrYMx-M10VHLnIufW5SEOYnN7jx_HwNPyL9FSOsLlN9JHx0YiyX59VccThOtY9o1Wd8guRBCcAGAU_DJBWWIpzQc9D6jVBBPgAZtf3YLjcTK1g5ExsFs4e_NlXoxED5TBoMMGfzxdUp08IzBbS32fycAzavNyuv7T95ZspD1KFYyo0A_LzW7lR4LFXoQnNSWHmuDTPyWLQvYKVFNiK21HWwBOAS1yMLM4-eZhLBMpGpXXj7UgyXrgvVkCqL1CzxohkoqoDX43qrFL80xLz3wOUevdfWopRFm4Cz1BaYkeXdRJzzaCkuBz1ynbNEu618bbxAX-v2CjNj2b3H_Cjuduf3GqyvlvId9llcHe0O7hj4Il9amI1TlXNNnIkj2kwG-lPWnVkOr1R2LcieNFx2zbwEIx8ALraqNW-4KvQX72IJuYZQG5ZXy2Q7_PqMYJRMAcJaigPtw2qM3lAUFi-X_xBR6bydqwrKl_gXWanm3qXMCpoUrv98a1gX7yFzBvCczYC9-zTSFm4uFvX49CtM5_j6_6a-FYiAC3vwREmydA7dCJmSCi8zk-nL43uvZeknZW-Nf663xXQOl90hNNDXSDTw6NbRok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=kq6JDAsuHpRcOHbMnhtsruWSezIUH6Pd0LHmaZTreYwYHG5iG2eW7AZACIfWYOWc54DRbhXfXKMjVkrGhakIGKt5EDbdXRighP2KvzlxsXdmKWeGmWoG-9aWBX6MA9_WVZzpsxJVtwzfUhwVAye2hFi_s0x3gpCwNhlr-xKm1PXCB0o6ZuYsZLCJMVT5eWqkzffiFryFcS45jzmZYI2VFmFr27RhiKu7tvZphsPqWkZ7jKVmCRyjZ1ePys1mB3RpAvvn16ILkB5BAIVPCaJxuKFoX87A17KgiOlwp5UTk1vWXE0HebPwlm7ZyAS9S3Ai39fYJdUqJXmEBkidJuzynQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=kq6JDAsuHpRcOHbMnhtsruWSezIUH6Pd0LHmaZTreYwYHG5iG2eW7AZACIfWYOWc54DRbhXfXKMjVkrGhakIGKt5EDbdXRighP2KvzlxsXdmKWeGmWoG-9aWBX6MA9_WVZzpsxJVtwzfUhwVAye2hFi_s0x3gpCwNhlr-xKm1PXCB0o6ZuYsZLCJMVT5eWqkzffiFryFcS45jzmZYI2VFmFr27RhiKu7tvZphsPqWkZ7jKVmCRyjZ1ePys1mB3RpAvvn16ILkB5BAIVPCaJxuKFoX87A17KgiOlwp5UTk1vWXE0HebPwlm7ZyAS9S3Ai39fYJdUqJXmEBkidJuzynQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftGqv97mWqx9p8AEJuWHlxAzPRixS6kn3Z4kD-8iFK_BT8e7y9LZWzgmJYHIAt0D2bN7Czol-C7EzRL6N8qEO7J4Qifg8uy6BsmCigUmdMzwQ6ySZj0V4OFLpH0AVhGvF6XvBXf1ltgOLfk_aMQ_QJVJhM-jKRiONXaM3EDmTlYZef9pZ_RzO0PQ9df9wvvuej3pjpksH0OTaiOso-58cz9Rk3q_0Z7Verl0a8dlOHYiaQTPeDyBKrylYdDEIn2i11INSnHA2A2UComcNFSsTjlAlH2jgWXCCkd3sP5JKCSVmnhzj1HemB4hR13rg8-wCX-PZwXSGnDTs_fJOnJYYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JahzQackSHeKVHl37MhuwkEV7Zni9qkFla1aalxDZev4Dq-FzR-5m9qEuegT5Wg6jFuTjLDAk0zhzpil5U-aa2gbNHPERvi6D6LZguMIA4zNk0y2By0l72NL_LmVaC3rCHIyh2_muklArtncJZYWEuahY5Jn7kWsj2Ay9FUEay2fpiW6Pdm2MU7P2j2xt-NMMrcdR6YB8QWZ7q_J20Kj0lFkKgFfgN8EYTDxQXMnpXaApQqU_yD4fCvFkPYsJ9UmvD1CUQQ2WXB-BMWQaFMdDrgxZTZTjDvDBN-ujcX6Om3r18PeRytT5SjBmK4oXQxY4wQdvxNRwK5rAFrlIK2dbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=fKdCZ2LSEYeJbxM9VilKhaI7pwmah643woAgwi5t_FD_ZQ8XwH88jIkXk5e85krI4OFs29xTyHCaWE60TpDWf_jV5uBoUA60MbHoG_8Au-YCUrSaah_fFdrKig_w_PSr5meebm7YoeGB1n2BjhoZb-JmXI3mLKWyaruc92BjAyZa9hLuqV6nHS6SJZkY7g4mX5k0sReOPATLRGdy-ENTrRV0RmLsuweKOJqnIjUW3KDPCI4BPTjdzxYmdZosy8ZKQGOk-pE3q1pD0rEgz0BAVJS21vuffqjKrLQVNn7lmk1S1ZGdfQjft0axFx--eJ3KC9k8BIyktO0rrAuu7f1TGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=fKdCZ2LSEYeJbxM9VilKhaI7pwmah643woAgwi5t_FD_ZQ8XwH88jIkXk5e85krI4OFs29xTyHCaWE60TpDWf_jV5uBoUA60MbHoG_8Au-YCUrSaah_fFdrKig_w_PSr5meebm7YoeGB1n2BjhoZb-JmXI3mLKWyaruc92BjAyZa9hLuqV6nHS6SJZkY7g4mX5k0sReOPATLRGdy-ENTrRV0RmLsuweKOJqnIjUW3KDPCI4BPTjdzxYmdZosy8ZKQGOk-pE3q1pD0rEgz0BAVJS21vuffqjKrLQVNn7lmk1S1ZGdfQjft0axFx--eJ3KC9k8BIyktO0rrAuu7f1TGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdadaEvu2GOrHe5u92rZ89B-XgCAC_4D4KXvUdb-fRemZlQAOu27zViDj-KunPA4llXsfI4MRLo_0eLJwYUqKfunlzNscGORlRZFswmQJAQIA17I9HRdTWCgXAaw1IwCkHO6vEScRgbUgvFsKkDhDEnKr9h2nuD2m6LBAd10pKmseiGNiF3lbTW_A4JPl2qu8wnC_jsel-YaVjQNEr8HX9TggLtgkoHBdjvHbaTzEvUGn_uzanio5SMigtt8jsn-bC2w0uQyf59yyuAkNhzJUxPSbSXiihRBDRwLe0QmCtRNEsy27hJ5ELhIpaOgj35aNAEGU7zr5cQHnKxc7dztzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/blxxkpzKVyEWLqe80hEckMuB4ClOSskJG-YJTPVXQA9RsH4kLRXQQb6JXfrW00Vyv0MzNAlJpy9frTI39sYTAnKK6nF1114KlDwnOtHJwdZV2rird373mWzT_mLywA9IKqjP57LU4GscEr3ADtkfEoAUJaJZ7ZF57KgJ4OMGkbDwJ6hC2ZEXIqtB6Yo0SqwUUYwTh0hjUQEVO-SxTp_i9jw9Jeg3vR9s0lnDrqWrNOXWcB3C_dgpAwCAP5cmKBz-0CSOGMsAQqFjlVJ5SNP8yFikWwLSR1a56JwwGFDMSZYsmHC5u8vBurTBjKL9m_e30n08pdPwCOSnDZDfVsfisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSVprIBFPjxA-4g8pipxT-61OYQssHLDsERWV8uk-6eHzwBDxYR_Z5TkC20k_5Zam1Hk2z5nV4ycGwVBbMcuEAiPNzvSNxiqFRPbLn2bbIe6dU-GWnpdBcqU7nyDi6UZAzk8_zQseHQUwaRhphxERtAQsGxUx5HGB4YVDoQ-FYAr2wIz_7gyrwJvGNN5faWP6cvzZYx-admlUgWi6pxz_ptKs1Uh1STqRTaeJ-Fr6KZbm-uPxrDys0_iI4MGHB9Et8l2zKoeWc1nVqpLNh25xLl1cdtTxfh5_dLcAQPiyIZvzw_msLc8-ZtdzgXr0F6mmh9QQzEjj5czFloZKQoNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBOftHfKWEV-_dCtPAhN0PzVG9VjdbWIfUYMKNhc4msfxrN5r5i3JPymqsx6IxnQwu6ybu2UEF-JALoz4nCbp_jC6OVYmq9gy6jAl3mqjUz4Fm0jzeaJJyx173YFTMPbvfGIK7uZCfFw6tV7Kpbv3LcfaNTleMlQ5Hj2-AcOAhxzK1GSwDCQJFpZGyhDVtMq5nQcDRWe4Ugm72AzYsjWnKOjRJq6gxdkpdzNBCV4InsP1O3bdwRQ68KIu8vT9sPLHVBmlWNocuRnISFcKrQepf-gEo20IfeoumDLAiw2EqSyUhvzdI5IwAIL6Hc3p-hQhlp-1-zn9NB2Auha24RXOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qmSmXE8zDsuHZEeBT4iwEihUAyCmOaJ6vuApinnduecOXab9nZrNrnnzt7YqhMqEtxD6mmIgzR_SnL9AT63rAl9Ww_kAujIQ6DJI4nbvbyNRubw93M8ox_fhNur2aBhAIzKG2VMFObSV69nqUNR183Gyibw0CdN0sVgsz6E7mFvoXejI06Vx5p-XqVpx8OwT18RMYaQkgqX-LQAoySETFe-lagS2SplXWtzRAkh06IzOsnJywfIPQAkGE_VMqNeTLcWcPluCBW2tc7rlprdNgPMuugI9XQULiISdz2TpK5BOn1Fm0Gg7H8A5DIsDE9Ds9PMExYaSsHezq7Zj-OYoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca061z2uCH3Zzq21myvmas5fP5pbWBCYSkzOc0pJEgbRdEiGlzB0BXB_xyM5SMLvrM04qfT7lH3mv-m0XwIIWg37LXIn52HXTX2Qr2NUKO97L9doQMlg4H5YIzhtqxgCzVG2Xds-845ZDRdes646xcL6mZ-1cL68iJoZnc6K6so6ZPtsiwdnRdWXE5JP7U4oaC1belNYZmeNilJ0BMbgdudigjvFg-fW34ewJM8DATIc15GuKJ6t5OV49ZQhadRzPgE1VUbmPhpCIQbA7bSsE2KyOWZZr3oQQqBsyDvIEb8vhPOKxo7UPduwLRxe14U-LrW8_sl_SnhpHAyhAV2VMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldm5LTI-nyb-OMbTRMEFIgni-0Bqj0hYA6h2qg011PVbfxc2r6gUsDynMDf_lplvFwaBWk2aNX1gsRoXvFHCexZZ8SXXCdKw4A0Vx9u5n6-qN6y0Z9WSFUvvdBxh00Fm-Ry3Wep-7ieanZOnQAa39-IHtCwchwf9EUEFOKwe06TMDr1PJwH0SGT0pZwElGxaVlqlyfW7bCAieoW5dsBH3ACdnkBLc88iPpFS0yRBepHBTo13k78Dl15-86So9ABQRWl0lPAIOSuVYgIAVRcqdNZy66d5lAXewM00RD7fdxVh7_TaEqk85jp0YvMVEcVP4UuX_uGmdvUto5xFY5g26w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HgUTASDWTF30fZ1EhjKVHKT-5FrDwlrc_d028Uq6FmlWr3pLNIILKv9UjHHxCCqH0EWdLojXfxTXYz4_1SznzR_V9sRt9Q7rflllqNym8lkR7mThpg-R1RRv_Ej5qDzGZpjZY4z6vU-AogXuxwvIf7Mjgsyi5TQyoG_inGZ5kcsn0QnW_lIq2Y6-GQ3cMgt7U0Na0rAtO7LT1-VaKoecRJMYPwjDMOCIkFf7JY0Nsg4XDGNsjVfl2LyFRIAW-D9dc-fPZ8XLDuv5hH1Ymxno8pJQPRDS6q7F74RgIRuftSvaH40wzBEbgJws21dJ3fjhxPtz8xe_39jgTrDnVjP1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6ZJwlXSLKAB9BFM-muABUQH177OqnkT2bIMgl91e7lyDTEIgidN-dAHm7v94eDLA1N8IgeMN-L3Er2-YjZRK7arfzjH5EQZ8vR7K5vVWzuNnar1_ZOKcyuDesTFx_wJKDiYfMCp7aNbddWoYPY3nnC4fy6lx1ZOqgUef9J5uQCf6rmIfl-YcLoMe6itpQXB0pSCosgyVlDlcbq78LSaO-NOjUrlnqSeQuihL8jqQLD4Fh_AL1-nirAMjEDtfIlku1xseBzGaKm3p2aSQvrM2sd_LKkvLjHBXGvz6BA6hSEBZ-5cEe3OD58YHfmwhpVxud19DT7O_xspxasKl9bnAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNHfdGTIGwor8mXlI2cm4D-QcexfKWidOdaftXwXTOGlNmacK1kolBRQ0olUuPKX3H3Xonu99g_sMKGwJ9i6lu_Y2ES96VzsvvdUj-KabQZkGiT0rmi9CuNFR4qxAO_-Egx44O67QeIfEI7256gdANsah8ZVNICQOVupWEzUEl6RoiI1frQLxsBdy38aeEr5-fX92GTju-b8I0cyJNX6FAaJYyFr-_ZSN959UahXQyWs7dA4Ru_nnEJzgKnndTs4kc7ieitg0ZF_jm28CMX4CAFuVwufVgTRB1ykQmbHqt96Dw-eWjR8IWZiyw7r9JZkiR5HgCaXVmISqvPwY_Y26Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQFGw9DtzvrKSXYGAhl2im8rGWIz6Cm7Du1VyU33yzLt57ajIWQCrHjgL_CNL13iM5EYKLXcMIRCiZx6rlNG_MXLFpAi7D6CM1jBI5XLo3Trj1xYXOXVett9wPsXpD4FkWFKL8oJHScvOH2eQFxEkSCcV7LdHiwrAQq3kcIAWl-VxLrWYRx2U4WcW32UtapR-Kb6kwxTChiCNiKMoCjLoLFl8_LHO-wpHxFZOpG-pmVz5JfBo1t3oudS1E1knChTrrlj_myMB1MYlpQoKNQrLCUyg_Vs46Rk70dRFTPXFlqNXi7oCOimYPtroi_o-9lI6kK3IVFEJpIlql4jMsi1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=jBw_Moj1Rx1M-PlKbj18kXfBuWLAIpVB9TzAD4-XmoxztLksK9gtCjWrK8se0R-zZO_b3IgQxRN0zOsDFfhUKuBeq6E983uAs4SISxUFdtgHB1H1RyJAQVMlmA_vKut1WOmhJykHhf-zj9LohEteNZoy3EpgiEGoFx9lTAp9DBHZa-UlVZbh1coCxHbk901UgpCdlETjRF3U9ZS8Uan95aUhmiVpEYXjRqYEW6nGxAKIYI6jr8zudIayzdZA1uj3suVTaaPjPLb6ioO-jjV0Q_2a5ONHpt4QNRIyiwBdJvQyzBO5rxCgBhHLOeAbc-VbRz_xXRqYKsv5PZoDS0SOWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=jBw_Moj1Rx1M-PlKbj18kXfBuWLAIpVB9TzAD4-XmoxztLksK9gtCjWrK8se0R-zZO_b3IgQxRN0zOsDFfhUKuBeq6E983uAs4SISxUFdtgHB1H1RyJAQVMlmA_vKut1WOmhJykHhf-zj9LohEteNZoy3EpgiEGoFx9lTAp9DBHZa-UlVZbh1coCxHbk901UgpCdlETjRF3U9ZS8Uan95aUhmiVpEYXjRqYEW6nGxAKIYI6jr8zudIayzdZA1uj3suVTaaPjPLb6ioO-jjV0Q_2a5ONHpt4QNRIyiwBdJvQyzBO5rxCgBhHLOeAbc-VbRz_xXRqYKsv5PZoDS0SOWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=Vc_N6MumlUk76HGFKmBAskWdNuzkdPBrpgg7coZct44H8vWuwuv29isMqMwTx3Ps4cZ9D1x5CKIMzszB2e3ZSUNNkX_g974rBxqHupikIWBAN8u2ewwSdWSY8U0OADemW8VNJ65AdeU7uqMRs_FsNniZ9LIUkqJckgweyegdIneEgYpicUEx54AKknqTVEOZ9YfrGXBWfFI9x_ZWiLMqfh_u5d_nWvoPC8G-j53pQipaHpjujNCY1E4VqAgt7GCZMMQ3cpO98W-VCAuMIhj4UsAM1lwa6ORqIQbRMp0mIjYZXvTgINddgc-xqRXx6CyBGWjQ7NbSElrFWO_95nI29A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=Vc_N6MumlUk76HGFKmBAskWdNuzkdPBrpgg7coZct44H8vWuwuv29isMqMwTx3Ps4cZ9D1x5CKIMzszB2e3ZSUNNkX_g974rBxqHupikIWBAN8u2ewwSdWSY8U0OADemW8VNJ65AdeU7uqMRs_FsNniZ9LIUkqJckgweyegdIneEgYpicUEx54AKknqTVEOZ9YfrGXBWfFI9x_ZWiLMqfh_u5d_nWvoPC8G-j53pQipaHpjujNCY1E4VqAgt7GCZMMQ3cpO98W-VCAuMIhj4UsAM1lwa6ORqIQbRMp0mIjYZXvTgINddgc-xqRXx6CyBGWjQ7NbSElrFWO_95nI29A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=BrweMh4iqpG0HDgKKK4g2XfpQn2T3B8iqyLguBE0k_Oz2OXZjDDXJ6rxpojTbNIbHVqHfbZdF5L-TFcuvYiI12DO-Lib3M42WaEydaDl_gdzW4GUM9bvTL674Iq3NXLz9DLlrMWHi3vDMpHe84GaYd30tn-tE2PtEkpr8H3DBULm0TGkbBQPgJoDKO-Fjj06XxSADS57PyS-SQr4D0USdZXY3D3sh1K7SByF3JSOj7mIg9C6ZhE_EEimZlBrlEuGiF1y6LX-pez0Ojx0psLRRy0bjHiLOj4o4wsqCDQ8n4-8Bs6Q81B98q5Jc1UYXeWFhU4oVz7KTowO7AdzbcnKyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=BrweMh4iqpG0HDgKKK4g2XfpQn2T3B8iqyLguBE0k_Oz2OXZjDDXJ6rxpojTbNIbHVqHfbZdF5L-TFcuvYiI12DO-Lib3M42WaEydaDl_gdzW4GUM9bvTL674Iq3NXLz9DLlrMWHi3vDMpHe84GaYd30tn-tE2PtEkpr8H3DBULm0TGkbBQPgJoDKO-Fjj06XxSADS57PyS-SQr4D0USdZXY3D3sh1K7SByF3JSOj7mIg9C6ZhE_EEimZlBrlEuGiF1y6LX-pez0Ojx0psLRRy0bjHiLOj4o4wsqCDQ8n4-8Bs6Q81B98q5Jc1UYXeWFhU4oVz7KTowO7AdzbcnKyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=R8gwu63O4L6_y20xJoXSO78xZyNxJqeffKESrM6AiuqdZ7d-JxFBmTqkp40_fojjS20J-MqwO9VHA_MpOKV3fC-wvl8wuntO0cIo6C5ji4PGacvdGYaPMuqfQLJueVErj4KanNMCKVbOIIhUbxogkPaTlmL62WpT4MA70qHTcOMBmXiPjd_XRTMa3lGv2G_hp4TxLW3FXtY3d-5HRAtrflVUZrSlhXn-MKvDYrPu6vyT9f0Jwqmn6VZknXYWG2YoTQaSH6QvmDhhFy39jCAXH7hwDfR0XZpwNr5j9jj-2xt4yS2qZKeKi9yn9_C5pXqKvvsNt-nwZqJWl82vKzRixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=R8gwu63O4L6_y20xJoXSO78xZyNxJqeffKESrM6AiuqdZ7d-JxFBmTqkp40_fojjS20J-MqwO9VHA_MpOKV3fC-wvl8wuntO0cIo6C5ji4PGacvdGYaPMuqfQLJueVErj4KanNMCKVbOIIhUbxogkPaTlmL62WpT4MA70qHTcOMBmXiPjd_XRTMa3lGv2G_hp4TxLW3FXtY3d-5HRAtrflVUZrSlhXn-MKvDYrPu6vyT9f0Jwqmn6VZknXYWG2YoTQaSH6QvmDhhFy39jCAXH7hwDfR0XZpwNr5j9jj-2xt4yS2qZKeKi9yn9_C5pXqKvvsNt-nwZqJWl82vKzRixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sWrgqiePqmcFNfcU3oW9hfvZw-BfxtPY7lURU8QVy4o8V-fF-E_dCcXR-JmIowdHhhFZiyIgjSNOguKfMYIk5UiHVt59SB3ETpFoGBDPOKlBRKGnmY2c6MVBNg-wWTedm8FNUjwDVFMkfgJq0_4qdh0IG73ipQzl5-x9paqb0F6HzzmcwefMJAX1HF7ldfakLdZz1_G6bXbKHCDcEHDz7SDDnU-ugOTaFnJsE74xm4UyeQsMfFoyyKeGdH72RPPcg_6zMuwGBX8P6HSiV5RIL4F4ASDN_lxq888qlXnBjyGso3xJah4OKCs_loCzCxcC9kWHOGqrpw66YbFKEnn0rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez4TZZIWCkKWoBxqoMyBKl2Bh06NN9ow1lBm4F1nkBhino5kA5_dFWONf8BdCf8uNXi-Gd32qGuNcORtWkVgdsy0YyvzRy27D7MP-FjpXb-OUxbfYJcgUd7bcPrDSep2oOn6Cqj1WqfrBJv34wuY-WhfOANpNm3lh59f852ORDKRB_ZenD9rtt6DC51i-dJyzFkfxZp6kodcFEHRgF0VUWCJDznjPh46tAGGvx4vB6Bylze7f2c_MRkKY_FHYTmDCiLUkQ6oEyf3ZVvBT96c2XMyCoMMVysz5I-TRgbMlfElnNEAadXxkrEJXEzZuhMm_IKhaeYQa8guN5b62yXHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lco3jXLqkddpuDRa4jxrAdLsBhugs2er95Lcr6SclJoAs20xcXlwJm1YPv17d0xzpTUvpK_LnJ_CIuy8xcvYVud7Cg5KEjgro5ew-P3K3zXmBjSJxIE27uq7tn9nRkxyKTh0hu1CHUSEbfhs8GiIY0A2sgtMVMOHkg2QnRqQbOFKoNvwv7mtdFRzak49KLU63jxb5yTXrb-NfDwmfYslExc7uC1B9NqSpbYgaRIHMFGb7pT-50-n076YqjKChlh93c82A6Rv3VRTITSxykEsw7uxrVyL6GtQ62QWSc18qV8KYoPsUAs_YBj90hi74o1tIU1BSO0LhPb-VxI9mClwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=ApwVUEt-uGCimYgwe3B7E2Nu4m-MIhO2nXY6NGfNx3dxSxkUoZ8R1xF3wwMn1zhWuW6W7rlD56vnjToFNWCwkKJG_nJcE8QcenbdUkVldPmPtWRZosEVVbzD1Rc9nHspMMuxgYRv9xvHbYRC2XJ_rq-jI9ZSdUOexIdIwfeW5C7J_yMVmNagsj8j6k7Sh2yvs3WnxO5BmmqoBKqp15aGT2yPZwhPUkl8rv8nWo3AotyoMbHqcd8Vbjj_iVo8FzfSXoK8pT71WNz-oUwh9yn8_Q-KVHdJJ-Aeyd2I4-8Si3H3bswES3x8UWX6gW1v8qpYjH4ByD3hpP2lv9TjTXeyBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=ApwVUEt-uGCimYgwe3B7E2Nu4m-MIhO2nXY6NGfNx3dxSxkUoZ8R1xF3wwMn1zhWuW6W7rlD56vnjToFNWCwkKJG_nJcE8QcenbdUkVldPmPtWRZosEVVbzD1Rc9nHspMMuxgYRv9xvHbYRC2XJ_rq-jI9ZSdUOexIdIwfeW5C7J_yMVmNagsj8j6k7Sh2yvs3WnxO5BmmqoBKqp15aGT2yPZwhPUkl8rv8nWo3AotyoMbHqcd8Vbjj_iVo8FzfSXoK8pT71WNz-oUwh9yn8_Q-KVHdJJ-Aeyd2I4-8Si3H3bswES3x8UWX6gW1v8qpYjH4ByD3hpP2lv9TjTXeyBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDuxBsghF7gOj_kGN4qqJU9UFAGUPCTRn5O4yW_vgb29Il1BNmJ_BoLjn8gWNGyQr0BwG6FZTw22OR1L4zricVOoPKaBiGO21CjlfGjQibe1Ka2paI_xVCTmaeZzq1dxuJUkUAMaJg3djfCsg3o4_oQr7a-gWMfZbyScBu6VIkB5dkYD0hcS87WsuR4YHa37eyruPisLf5VPzOKoLir3QJtK2gv7prDy8b-zHyDFfiFx7wDE6TvWC2PRYnni08WXVAwM-XD-q-wkPZ_DKvQ5d4UpRhnZRs_ERtZ8ujI__zk8avxH8Hv-xgQYrgRaXDt57l8YzBW0AAqaYdPcGh41qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=gk0bu85edetw6dOS5AY07EqAAXBEnetIg9MONgf20H_wTAzD9QCH4g0bfC4B6901qRY9YRGs2e62Ick7sNz9w-szrDp3LSw5RoUsBHHmR2wUW3nP-eSQTu1q8_tJT945fia9gTegWAhGFmzJScm4TuxeAOyBp2iz-X0-q_5uvZHGRqL6TOizYooWcpG5YmvjVNg4v7j5lfhaM9wT9joDJpdQtlwu6mOqvAPRGusQKp6DTdqy1Va62hVM784LGH8H32Odz5dpSXTmji8uBFWSUSv-W9najgG-QTGCXBNLglYdgEXCTwQj0Rr8Osu0m_7CyqGuAb8m4_yitCu0n-FsCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=gk0bu85edetw6dOS5AY07EqAAXBEnetIg9MONgf20H_wTAzD9QCH4g0bfC4B6901qRY9YRGs2e62Ick7sNz9w-szrDp3LSw5RoUsBHHmR2wUW3nP-eSQTu1q8_tJT945fia9gTegWAhGFmzJScm4TuxeAOyBp2iz-X0-q_5uvZHGRqL6TOizYooWcpG5YmvjVNg4v7j5lfhaM9wT9joDJpdQtlwu6mOqvAPRGusQKp6DTdqy1Va62hVM784LGH8H32Odz5dpSXTmji8uBFWSUSv-W9najgG-QTGCXBNLglYdgEXCTwQj0Rr8Osu0m_7CyqGuAb8m4_yitCu0n-FsCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=nGoWSi4fIzTzTci64JvmOLbj47X9WxhYlHVD-RnpT4q24R7JMUNSB5CPBV256LB3mkuZExKc4xcFYaH8mrDOMpwFyWfAaH5EfNrFw2Qoy4zvmI8CyUkgV7CLM_SKmYWa-JISbz_sXRXG33WbU3hGsSFJs0Jg6T_Krj-U5xdKlRkQulmxPioq0dHbcmsyKBv1Is9Nf-GbwrtGORu2txlAnyiuHoDHctfIShJ0S-FjfXL1Ho8s6_SaoBaSPGRJaHRVtthoQ8UyIesTkdtdnDKifWakkynjY6BS2IEHKLq3KPH_H21eKAX_hjI1egNBiSv_CA-xr01wQzG65Br0SK99-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=nGoWSi4fIzTzTci64JvmOLbj47X9WxhYlHVD-RnpT4q24R7JMUNSB5CPBV256LB3mkuZExKc4xcFYaH8mrDOMpwFyWfAaH5EfNrFw2Qoy4zvmI8CyUkgV7CLM_SKmYWa-JISbz_sXRXG33WbU3hGsSFJs0Jg6T_Krj-U5xdKlRkQulmxPioq0dHbcmsyKBv1Is9Nf-GbwrtGORu2txlAnyiuHoDHctfIShJ0S-FjfXL1Ho8s6_SaoBaSPGRJaHRVtthoQ8UyIesTkdtdnDKifWakkynjY6BS2IEHKLq3KPH_H21eKAX_hjI1egNBiSv_CA-xr01wQzG65Br0SK99-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=NW-CbpIBwzSKfBKpU9visdMAr1tU1FdWL2GmenTZK8RBM5Xru0vSYLxM77YucdbIhTEUV22RsMmC3m_I4Hr9W4Qhs3tzgClafu7NGmpW0EdZtEMHK02cML-wBb02d-2ioK3olu-zJIgFGNU3VQXhgl4L0VfMe63G2UkeVyzssjVYK8LtcoYaydSCXPqkq1dims9B7oeQ-ld0axP8gNQIjjFzM3YU-hCkBZWyEJe2kslQ_-p9kt-Tw330Ahy3klyoXYMYSCmLhgpaYdVmJqPyIdZfWzvahtNhCWM-M93vLdu2MrVIVR2Oie1_kK9Ld_SJxUMO_0rEGmWafUrextNRNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=NW-CbpIBwzSKfBKpU9visdMAr1tU1FdWL2GmenTZK8RBM5Xru0vSYLxM77YucdbIhTEUV22RsMmC3m_I4Hr9W4Qhs3tzgClafu7NGmpW0EdZtEMHK02cML-wBb02d-2ioK3olu-zJIgFGNU3VQXhgl4L0VfMe63G2UkeVyzssjVYK8LtcoYaydSCXPqkq1dims9B7oeQ-ld0axP8gNQIjjFzM3YU-hCkBZWyEJe2kslQ_-p9kt-Tw330Ahy3klyoXYMYSCmLhgpaYdVmJqPyIdZfWzvahtNhCWM-M93vLdu2MrVIVR2Oie1_kK9Ld_SJxUMO_0rEGmWafUrextNRNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlXRywWo-teAIjc4awvSFBdejsFqfSpNbA7MSV00lzCWtI-uCuaiHDeH5G9RvBeQl1uIizaPKsfjAYKUExCZEQeGc8RbPPtKjgMUsQidBY8u3jl9cq4ZyhMDRkW2ZvqDVupOs-0TzUAH4z4b7c7uv1tpYbbn3A_8-eBlyxkdZeXiiqt4mRwidydj18AftWynTy24rBtD2tLWiX4UWJBwjsKiqyLTdWw1JVRLvri4xFEKW-YxBEjCgc9OVmyQ9i837kAODRsauxP3xFplX0gxmxwoZy4AmWz8FmhWUfQHt4cAxGyKuT88-cHugeJXacxRrw262Ev4qr_lLrM4BCTZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=hMumC8eZfV36AqXlUxExvuEY_MC5DY4Yd2n9_BZ53LFJ_YG11oC3lJIaIgdKCQcLzEakchGtONS_a91i-eIn0J9e1tVaTMsvQF0S0uIETQtY77TAY1buf-XKW8FZCoccANbo4jnRdpXmrVq_7UqA5ufY_xoHkU8agN5YB1gJl1Bkn40j_3fLNIA2uYNSyAO2nGX0PXl1guWSNESf2O_JifYVeaOmSphMF19ZIrYt6LTBc69MkvxviiwpXS4UgwaOsRmO85VMT2k5w0E05MJdjn9wM8WM71DVcT6VfpKNknqb__IyT54m_Zep9SckuqMPiPEIQGFzOGsEuC9o-hTqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=hMumC8eZfV36AqXlUxExvuEY_MC5DY4Yd2n9_BZ53LFJ_YG11oC3lJIaIgdKCQcLzEakchGtONS_a91i-eIn0J9e1tVaTMsvQF0S0uIETQtY77TAY1buf-XKW8FZCoccANbo4jnRdpXmrVq_7UqA5ufY_xoHkU8agN5YB1gJl1Bkn40j_3fLNIA2uYNSyAO2nGX0PXl1guWSNESf2O_JifYVeaOmSphMF19ZIrYt6LTBc69MkvxviiwpXS4UgwaOsRmO85VMT2k5w0E05MJdjn9wM8WM71DVcT6VfpKNknqb__IyT54m_Zep9SckuqMPiPEIQGFzOGsEuC9o-hTqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSb-5A4Be3F9SbnN1y65D62Lgik0pSwMmS8pWr9uAhz5QghicAltgOOhyame9IecKCEREkbUK5eh8YVw7F16q4_nqaIjGf78aM66i1xAd4EvreaI1rgLIMYPA-iKkmUcS7Zcf4excOQ4LlIuYIIBCUHdQum47HgvVhJXGRhiPYir227-jp4aN-nSw5J13-j4E--c7NJ9wEehiS6NFTM5cBcsYfFtz4XZ9rnD8A0U3Hko_bt9NMGhKbqnXCs2FnxQYNi5LT6bq7CmcC74RerxVCpRhXDop9WlCpeniQz6vDHYvfdI-iQuZYw_22jpN997QYyVwcZLAD_J_GuoErwXNV94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSb-5A4Be3F9SbnN1y65D62Lgik0pSwMmS8pWr9uAhz5QghicAltgOOhyame9IecKCEREkbUK5eh8YVw7F16q4_nqaIjGf78aM66i1xAd4EvreaI1rgLIMYPA-iKkmUcS7Zcf4excOQ4LlIuYIIBCUHdQum47HgvVhJXGRhiPYir227-jp4aN-nSw5J13-j4E--c7NJ9wEehiS6NFTM5cBcsYfFtz4XZ9rnD8A0U3Hko_bt9NMGhKbqnXCs2FnxQYNi5LT6bq7CmcC74RerxVCpRhXDop9WlCpeniQz6vDHYvfdI-iQuZYw_22jpN997QYyVwcZLAD_J_GuoErwXNV94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbEY3Xh0QYQ8xQq4SVHR0DLKhCjJuIYyGTK07tsQZpPBOJtJEC3h1sTsYIXOShGGPdsN-0So5Pje98mfF2H00ntx5DVms0jPcheYAB4wfItcN5LIvLf6Kl5ISaaG2BZdW9nm3G-t_tMAQxSDMKRJqQr6iBDsp6xy2zWHYBBNKTcvFCcc7zfXQKHh1UHn8BzD1ytPTSIj0AjtIM5FuA6f84RRJ1RTQCZ9Yhw0pboKmEFPP684hNRBsWEp0wvwQIah8RN68GvXXzLKAYlKL8nuB0b0rhDxop_yXARgyeMMc6cXD0oe1tbUS3dUSuCgeGCTGnlpl7xO1uR1LkXNcleVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=VU423yoMcr6-RNm98zApV3etadUENIoygvZ5sPIux1Ap4iA286IYlZ4DnnXl6d1lhrgpVjWu0mb3VOElkdqGVqK74tEU6NtPCnI4tph4ANjuzDsjCPmqzcWIYDjsA2oq4OZQFS8nmaU-2pOjI7F1h_kcEtDNlO_S6uQpUZ1wz-_jHDRzKtbrQXrfOxahmPcEziPsF3IPXjrSfxDqiHq_C9385jgFbLPeA0GvsZkrn9DTveFOikTNf6u4L_8sYWLXVYcXw483CpPhUX31ir2Vh7DDZ1vV3eP7hIsnH5IdC_zbxliAFo6sBtVe8GkzOqa8ZhgztBaipVwgoTo2kve3qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=VU423yoMcr6-RNm98zApV3etadUENIoygvZ5sPIux1Ap4iA286IYlZ4DnnXl6d1lhrgpVjWu0mb3VOElkdqGVqK74tEU6NtPCnI4tph4ANjuzDsjCPmqzcWIYDjsA2oq4OZQFS8nmaU-2pOjI7F1h_kcEtDNlO_S6uQpUZ1wz-_jHDRzKtbrQXrfOxahmPcEziPsF3IPXjrSfxDqiHq_C9385jgFbLPeA0GvsZkrn9DTveFOikTNf6u4L_8sYWLXVYcXw483CpPhUX31ir2Vh7DDZ1vV3eP7hIsnH5IdC_zbxliAFo6sBtVe8GkzOqa8ZhgztBaipVwgoTo2kve3qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXsOBUdEyoMVkgoaKeiUETBZmx0OoJ-1-_GfU8rDOatZDNDNjscKdeM0v7nY6Mz9n_N1aYCj4aByIQkv0csr5iKORqcNc6tA6CBUMIV0tzDGG0XcP2mNAcmuthIfkPB3nKxfuylta5aQtx5gDNvUSWepGdt3VDuGVE2BWUCDpnJbGcQ1WyWw9mKVGL9ja-De_-zz1i7ISjohEwjzz5lvm4tAPg2eR0rAv5PQmL6BXfgwRq-J7MQBteTYHUjv3yL-L9heGAqBpWFp-OXIzyi0ZgcTsDs85z3SpVb8RvzJwFBzQ2G8H3ogz5J4qql8c8-t-xS_sMTohHRmOghd51y9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=RtRZDhhhBT_Y_Np4MUssJ5icFpHhFx7Ea4teY6Ixm3-9nHGcgQ4-0oRKvIJlFjp5B6jU1GkgvwuH-xJzembqBkSnfj8qfOTOZsMyEQevUm4pZsJJ31n7Xy12pUpQR1YTeAfJz7LblxEVl1i1Nq8QjvPvX0JdpSPyVhR9JlL1GG4bdYCUKklq9npdmBAF5oSIENymQVBaImYUxq94ySTTfidNO4VuIe360-zv6gWs4cS2fq5UExTI1tcgvuSARAYOMYhbbzGr5cnvxLPUw80JDxunGE6Lm3u0U-M9fbdlz69UphV4HuRAFiPCqmneiqBJNIApK2HU9vfduCUb3Jggi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=RtRZDhhhBT_Y_Np4MUssJ5icFpHhFx7Ea4teY6Ixm3-9nHGcgQ4-0oRKvIJlFjp5B6jU1GkgvwuH-xJzembqBkSnfj8qfOTOZsMyEQevUm4pZsJJ31n7Xy12pUpQR1YTeAfJz7LblxEVl1i1Nq8QjvPvX0JdpSPyVhR9JlL1GG4bdYCUKklq9npdmBAF5oSIENymQVBaImYUxq94ySTTfidNO4VuIe360-zv6gWs4cS2fq5UExTI1tcgvuSARAYOMYhbbzGr5cnvxLPUw80JDxunGE6Lm3u0U-M9fbdlz69UphV4HuRAFiPCqmneiqBJNIApK2HU9vfduCUb3Jggi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=UVC4sM9h2NS2sgzYexO61DxsV_6VhcIYSlQitX0-uhWc-1No6oT5KT2FCmKGMm2gGeIsVwFkfqaNdhEqBqdU7RA2RU8_cA0gD6ZYudUzh8s9GN1nYEnO1pTUubXH39NRPdcY833XULmFf7G1tnTj7oZ_6ZhQta997OMGj6ctjD2r0eEEN_L-oDWINfNGAe74e9nQQL3LY-BDnv1dcU2lAQBIYD9UjRhuh8PVPpJ_4frpYGljKEALwN9sdLn95xdRRxFp1x2M3vEOWG8y5CDeQLckLOiH5PB0OD4vAQjzFeOqAQ3R1_L_TqoBUvPKhQVV4Rpsu-QezQOZHbvpG_g5sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=UVC4sM9h2NS2sgzYexO61DxsV_6VhcIYSlQitX0-uhWc-1No6oT5KT2FCmKGMm2gGeIsVwFkfqaNdhEqBqdU7RA2RU8_cA0gD6ZYudUzh8s9GN1nYEnO1pTUubXH39NRPdcY833XULmFf7G1tnTj7oZ_6ZhQta997OMGj6ctjD2r0eEEN_L-oDWINfNGAe74e9nQQL3LY-BDnv1dcU2lAQBIYD9UjRhuh8PVPpJ_4frpYGljKEALwN9sdLn95xdRRxFp1x2M3vEOWG8y5CDeQLckLOiH5PB0OD4vAQjzFeOqAQ3R1_L_TqoBUvPKhQVV4Rpsu-QezQOZHbvpG_g5sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
