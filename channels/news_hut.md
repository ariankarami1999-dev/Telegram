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
<img src="https://cdn4.telesco.pe/file/H0gSLo44wN019_qRbcYjQXGb3S61J7h90V2Gve4JngBdf785ZasJnWzh4aIhGrUOT8pN-OakIurkl4dC18katcpjSix4_3GMvqmquuZ8WkM1C32ckKjfr-PyYEdKSM5piFDc_9lQFSwuBu6kv9TXaqy2ZEiCMOFAMzByknotIZ_gEGwIYQE_GjYA2GcJ2HiHz_XqwdNQhK77a4_9KOXNSOaqYhUNJWETGWreX0T6MrHkXjd-P9iptwe2hQa_bDJzsD-kD6fISQQfyQszgmWi_jCWx6L9AD1sYLRA8ml78tv-HhmrPMs8ZBlTd7gP_sI7QyIkC-R_t7cqx8rjLvG4nQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-72957">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB1xxNrUN5VsrM968vwb9TVKAazN82jkEdXG2bZptj3dbzWSeksX4e6A9Ou_j-KNNPE85ehEWf60F5XGDLFmPJnxGDj04putwF3PQrJUL1aw2nl-Tn1TlcSNB3t9-mZHKLam93zsZjNVeYQVo_4pUfN895_zKf6Cgy9U26sRWZs1yaVV01ApdieW1E_vkXB9laNf7foIuRxoH-BaS1fZyrKMETmaBo4ZUKi6n3DwXjkkJClRIK3lEj-pK32CJTN-2D8EwrFGJmw3ctD5mvfX05iqxBInHQ5f6N9gmXy0Pa7ZMSdEtfuuXDGYO6XfeAvhRqzMeTXV1vl4ultNciigNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=bQdyH8X0cxIW5Ho1PLFxT9SCg6ZKZidCGBak0GyPPjOVhhXCdxfpRnu6gowOc41-mj2r3VBc3TlbXeAMLQtEaM91_BpzSbwibMh0ipH1aLzb9sm6VnLMVkU5qC9tLyfHUnb9bkGLOz76R-GNpiUqORgxHafL56kRvqZbRUy907aO_6j7b7conVkSUbXc9AMRjENncYVaWcwMxGzv-YAwCEjrxE4679eU5y2HACnjg5ToSNc_FF7BypS-GcWPYtrkKCdyxUcdgOHG1pyxjSwHU3z5DcXJ0qwJgLEH3n_JiTi0mZN0IlwbzGHsTVGuXoSJ8W-DzyW5Mjrd8yPNyL9Z8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=bQdyH8X0cxIW5Ho1PLFxT9SCg6ZKZidCGBak0GyPPjOVhhXCdxfpRnu6gowOc41-mj2r3VBc3TlbXeAMLQtEaM91_BpzSbwibMh0ipH1aLzb9sm6VnLMVkU5qC9tLyfHUnb9bkGLOz76R-GNpiUqORgxHafL56kRvqZbRUy907aO_6j7b7conVkSUbXc9AMRjENncYVaWcwMxGzv-YAwCEjrxE4679eU5y2HACnjg5ToSNc_FF7BypS-GcWPYtrkKCdyxUcdgOHG1pyxjSwHU3z5DcXJ0qwJgLEH3n_JiTi0mZN0IlwbzGHsTVGuXoSJ8W-DzyW5Mjrd8yPNyL9Z8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر تأیید می‌کنن که یک هواپیمای شرکت هواپیمایی سعودی (Saudia) که در فرودگاه بین‌المللی ملک خالد ریاض متوقف بوده، در حمله موشکی اخیر حوثی‌ها (انصارالله) هدف قرار گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 313 · <a href="https://t.me/news_hut/72957" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72956">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=DX3TLaI1y0VWdUWV2naWEcKS3Dtguf3yjUk6sYyd4V6Y90ulnroYQTBHt7NlS07Q9xyK_Aw6hz6eYGKgx76vTEqUXfgFtVukOEtOp3UH7YPPhjJ0RPef_mpgKN5E5NaSOY3Z2hm45G2El_2npAtTTcP5fuUbdR9YK9cQg9wUa_IX41D-Vwr0eBGT7-xwA0TQ-ZvnJcghU-OTY6-G9_5zQO_kJGMdNuLc6Z-neexW4is8DbuWo5fSxiODS9ikqPKZ4YgO_RehFj2WfUT_V9Hp5Ufd8GnagVkTRsLCXqcfawJvjbv_8BdIIslDVqs0KL4GnLw2E34OvNz7xf9t8YCUVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=DX3TLaI1y0VWdUWV2naWEcKS3Dtguf3yjUk6sYyd4V6Y90ulnroYQTBHt7NlS07Q9xyK_Aw6hz6eYGKgx76vTEqUXfgFtVukOEtOp3UH7YPPhjJ0RPef_mpgKN5E5NaSOY3Z2hm45G2El_2npAtTTcP5fuUbdR9YK9cQg9wUa_IX41D-Vwr0eBGT7-xwA0TQ-ZvnJcghU-OTY6-G9_5zQO_kJGMdNuLc6Z-neexW4is8DbuWo5fSxiODS9ikqPKZ4YgO_RehFj2WfUT_V9Hp5Ufd8GnagVkTRsLCXqcfawJvjbv_8BdIIslDVqs0KL4GnLw2E34OvNz7xf9t8YCUVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:اقای همتی قرار بود وضعیت دلار بهتر بشه پس چیشد؟
همتی کله کیری: فقط به اقای بسنت بگید 3 روز بیشتر وقت نداری
😐
@News_Hut</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/news_hut/72956" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72955">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=RnibOGcfo8ekQim19LiMA-qUxipnE13XbcMZtDGjT9BgDEMtGhArwquH3CCacTBG5Vp7mqm-OdV4l5U16PqKuHGZxLB1IsO7UJOOTmU2IwYFoC9isC0aaySMi4IKLurPM3nrVxCHJY93YQi2K23RwA-0L2ALFc6yV6Mhyspk9mkEjxp2n1wXuNw1faNh8Jw9MavDLA1pAwG28xNW0CqpjiVeP__d5igQxqp3M80_c2Le4V7L332Yua4IuFbD57N6TGkdRvV61hUmHTi3e2ZT63sHS5EUpHKUOca7nOXcKUR-byvicROKS8tDsbUOqt5gAnHANqTkZtczOkLb2qY2zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=RnibOGcfo8ekQim19LiMA-qUxipnE13XbcMZtDGjT9BgDEMtGhArwquH3CCacTBG5Vp7mqm-OdV4l5U16PqKuHGZxLB1IsO7UJOOTmU2IwYFoC9isC0aaySMi4IKLurPM3nrVxCHJY93YQi2K23RwA-0L2ALFc6yV6Mhyspk9mkEjxp2n1wXuNw1faNh8Jw9MavDLA1pAwG28xNW0CqpjiVeP__d5igQxqp3M80_c2Le4V7L332Yua4IuFbD57N6TGkdRvV61hUmHTi3e2ZT63sHS5EUpHKUOca7nOXcKUR-byvicROKS8tDsbUOqt5gAnHANqTkZtczOkLb2qY2zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن زنگنه نماینده کاکولد‌زاده مجلس:
قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
البته قرار بود سهم بیشتری بهشون بدین اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری میکنیم که حلش کنیم!
@News_Hut
😐</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/news_hut/72955" target="_blank">📅 18:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72954">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=hKxK8TfugHak31d_Y25jZpamExEJqRM0tbdx0GaD9NS3OitrdOmWXZDYfwluJwM-ORLvw1T-Yv_mjxXeMZAatuwJda2pUEtp2zX6pg8_LB6O6cF3xwH6ozPmM_wMW-sP9lABaTyunwIkHwj_AZNHkXBZznoRA35gZVw4lbpoTCn1SpEwzYifQI-LXgLT1GeXa8I6P6sv-W4sQXEU46XnpMDHJC9EbTcM3t9t7FKDCCKR-vN0yXhjr2frWpPGF5ZfHd0JPP0uMjrAXhoE3WuJSxNWt2iP-1Cur7gklqURABHMge1JKvaqPHVAC3YKo93qyGpmJk0a4dwtEV752phe-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=hKxK8TfugHak31d_Y25jZpamExEJqRM0tbdx0GaD9NS3OitrdOmWXZDYfwluJwM-ORLvw1T-Yv_mjxXeMZAatuwJda2pUEtp2zX6pg8_LB6O6cF3xwH6ozPmM_wMW-sP9lABaTyunwIkHwj_AZNHkXBZznoRA35gZVw4lbpoTCn1SpEwzYifQI-LXgLT1GeXa8I6P6sv-W4sQXEU46XnpMDHJC9EbTcM3t9t7FKDCCKR-vN0yXhjr2frWpPGF5ZfHd0JPP0uMjrAXhoE3WuJSxNWt2iP-1Cur7gklqURABHMge1JKvaqPHVAC3YKo93qyGpmJk0a4dwtEV752phe-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌خواید ببینید مشکل واقعی یعنی چی؟ بذارید به لس‌آنجلس حمله کنن، یا به جایی مثل سن‌دیگو حمله کنن. بذارید به یکی از شهرهای بزرگ ما حمله کنن.
اون‌وقت می‌شه گفت
یه مشکل واقعی به وجود اومده.
»
@News_Hut</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/news_hut/72954" target="_blank">📅 18:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72953">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=EZRBh6v9kSOCsNod083HnVIz3dhsulIVirNvkEREQr6FAQgUXOtVuSQwC73QkBs6d6iPwZKUR8JUVwsHpQjUM4EMnEzf0mN9HMyBC-X4lA_owl55Erlkh3GT5X0-n4lD0jZwpfhtkzvjhR3p2NzfZVQ3-TV6s0hry3u_Z3exLKo6FTobtiEQtsY9lv4IqF2U3T8KKs1gNlNLXjTkghwL6uBa5JMh9ZfeyKF7spYM-2azj9aPEDailg8GGhU5plfR0HlXGNgb13ODeKQvxeWCt5XYz3bFGG_wCfGQWNZuZTmAuNnIL89S-E3nL0-XJQ6tnCrrTiWWk8zgN6W5bsivbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=EZRBh6v9kSOCsNod083HnVIz3dhsulIVirNvkEREQr6FAQgUXOtVuSQwC73QkBs6d6iPwZKUR8JUVwsHpQjUM4EMnEzf0mN9HMyBC-X4lA_owl55Erlkh3GT5X0-n4lD0jZwpfhtkzvjhR3p2NzfZVQ3-TV6s0hry3u_Z3exLKo6FTobtiEQtsY9lv4IqF2U3T8KKs1gNlNLXjTkghwL6uBa5JMh9ZfeyKF7spYM-2azj9aPEDailg8GGhU5plfR0HlXGNgb13ODeKQvxeWCt5XYz3bFGG_wCfGQWNZuZTmAuNnIL89S-E3nL0-XJQ6tnCrrTiWWk8zgN6W5bsivbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما داریم ایران رو خیلی شدید شکست می‌دیم. دیگه تهدیدی از بابت سلاح هسته‌ای وجود نداره.
الان اوضاعشون خیلی به‌هم‌ریخته‌ست.»
@News_Hut</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/news_hut/72953" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72952">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=FNI0-EscIdffMfF34OHfMO3NSfFnnyZljoGzJIC4B6Zlt81K07NKDxjGZJU1X5rR1XoX8o_oW22EdZvszesFTUlP0SbED7s4-K_9HFeJx5bYENe72tY1P2iq2czKqaKSStuB2JtkBVNjcscN0yVkVlVwSPJv9yRpL_gA7kOTq08URjO8x9_2GMHlwjKAr8tc3LTWDRcuVU-6CcWOt1jL_GmeABnBhMGQ1XP-aUfBqT0gOMUWHb3jIMllN4jNq4WOWhc9W65Ms3LvEZ_qNF5LydahvcEUeoJBuTI5M12wfWc4T7efBj4tRWTAI-tU9Ap0LzIwGSeEZfgzNLPlZWmh6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=FNI0-EscIdffMfF34OHfMO3NSfFnnyZljoGzJIC4B6Zlt81K07NKDxjGZJU1X5rR1XoX8o_oW22EdZvszesFTUlP0SbED7s4-K_9HFeJx5bYENe72tY1P2iq2czKqaKSStuB2JtkBVNjcscN0yVkVlVwSPJv9yRpL_gA7kOTq08URjO8x9_2GMHlwjKAr8tc3LTWDRcuVU-6CcWOt1jL_GmeABnBhMGQ1XP-aUfBqT0gOMUWHb3jIMllN4jNq4WOWhc9W65Ms3LvEZ_qNF5LydahvcEUeoJBuTI5M12wfWc4T7efBj4tRWTAI-tU9Ap0LzIwGSeEZfgzNLPlZWmh6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه پسر ایرانی :
سرمون درد گرفت شماها ولکن نیستید هنوز تو خیابون
خامنه ای رو خاک کردن عمو کردنش زیر خاک ولش کنید
خامنه ای رو خاک کردن شاه رو مومیایی ؛ ایران یعنی شاه
شاه که اومده بود دانشگاه و مدرسه ساخت
جاده خاکی هارو شاه اسفالت کرد و ایرانو شاه درست کرد
اگه شاه اومده بود تخم مرغ نمیخریدیم 50 تومن ماست نمیخریدم 680 تومن
خداوکیلی من تو این مملکت چطوری باید زندگی کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/news_hut/72952" target="_blank">📅 18:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72951">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72951" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/news_hut/72951" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72950">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxdc773lpC7wg_z4heSJt30WTbi0ah8I0khPTuTBEGVfhvh5NfDAU0fCgc79DQovo3BZiKz4hev5cWd-I1kEbIIQY0kAZ0eyEHL9pJv35KCWiuRoQd7h138i_KgJdjBtwCXwBnmgubh3X9wzf2p5xTtOaBwn9zd2DN_-lg4bdTQdX7g1RpVmS7kUv8XThyPP6ybE-lGbUW49k_htTW-JL_wdY_yWcc7MDv6GXqcMeUy-5IvihSHSb10yP49IMIbfokfckFzaxOLG3rD08sxXeWaIncS666B40Tk5dBiqDBWN5QpRv1Ri7JLwgcaJqkqo1aq2d_t3RMWajeGivsN0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/news_hut/72950" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72949">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=bPJX6hZ3PtQ36z0UOB5OfhQPicdaa1U83WskIcmyy8KCjwWHadsUAFvUpjibcFg0e5wS7Mt5BMXh1SQS1-7bLySFZRfD6vIbVIKEdzPXcoAZcjlVJfFlq1KVz6Bi_EDMZAkYjvGtUTDUF0wo7gEEAWrnC3FdVYfqgLJLfkh-CicGY-mOqkJHbKCCr0Jc9Nn_GkBj6C-MDLEyxSnpt6rZNZYFamxJeZ8Jj_lkmVtaXTHRF_wMyKq9t7g2c6tsY6tt9eRzCBuPHla1oapGkB589dLJ588MT59f_6ziVGfRUnzwJ7CamhfVxI_b8d2ruvpjJyvPItYT6ea0BkJPNC0Ee5HMcbfyZgEyu9_dfJ8CSB8FknqtiJHvL868pNiAw6xZaetCqX8pl5-pUYd3rrSaE-OREKzAqmL6tDkxZ0XYqHuHXAXZXVovZiysfNt_SqXddJ0iFDKArB8Zi-rdtE_LJcaW2LqfjcO_-JM5yke8--uZPfh6fnctGV1BuwhFM8pCDB0Hqc4HwBjM3U2uf5aeiz6mtz-yJLsgkSnWoGz8cBJa3d3_5YDdLRhDtHaEjUg9bTISMLLAtOkOXMJ2TlXEbyq8aqF601zmxCxzsveYnsSmQIwvuSd-Xc4GYhBViZv50uGWvGJ1Rl6F_RE75b-VdHj4YDiEUBHg0mSgc8O0ZCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=bPJX6hZ3PtQ36z0UOB5OfhQPicdaa1U83WskIcmyy8KCjwWHadsUAFvUpjibcFg0e5wS7Mt5BMXh1SQS1-7bLySFZRfD6vIbVIKEdzPXcoAZcjlVJfFlq1KVz6Bi_EDMZAkYjvGtUTDUF0wo7gEEAWrnC3FdVYfqgLJLfkh-CicGY-mOqkJHbKCCr0Jc9Nn_GkBj6C-MDLEyxSnpt6rZNZYFamxJeZ8Jj_lkmVtaXTHRF_wMyKq9t7g2c6tsY6tt9eRzCBuPHla1oapGkB589dLJ588MT59f_6ziVGfRUnzwJ7CamhfVxI_b8d2ruvpjJyvPItYT6ea0BkJPNC0Ee5HMcbfyZgEyu9_dfJ8CSB8FknqtiJHvL868pNiAw6xZaetCqX8pl5-pUYd3rrSaE-OREKzAqmL6tDkxZ0XYqHuHXAXZXVovZiysfNt_SqXddJ0iFDKArB8Zi-rdtE_LJcaW2LqfjcO_-JM5yke8--uZPfh6fnctGV1BuwhFM8pCDB0Hqc4HwBjM3U2uf5aeiz6mtz-yJLsgkSnWoGz8cBJa3d3_5YDdLRhDtHaEjUg9bTISMLLAtOkOXMJ2TlXEbyq8aqF601zmxCxzsveYnsSmQIwvuSd-Xc4GYhBViZv50uGWvGJ1Rl6F_RE75b-VdHj4YDiEUBHg0mSgc8O0ZCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
« سازمان عفو بین‌الملل یه کلاهبرداریه.
می‌دونید به نظر من عفو بین‌الملل باید روی چی تمرکز کنه؟ روی حکومت ایران که ده‌ها هزار نفر رو در خیابون‌های تهران و جاهای دیگه کشور، خونسردانه به قتل رسونده.
عفو بین‌الملل باید روی این تمرکز کنه که حکومت ایران وقتی معترضان زخمی می‌شن، می‌ره سراغ بیمارستان‌ها و اون‌ها رو روی تخت بیمارستان می‌کشه؛ تازه گاهی پزشک‌ها یا پرستارهایی رو هم که اون‌ها رو درمان کردن، می‌کشه.
این‌ها جنایت جنگی هستن، جنایت علیه بشریتن و جنایت‌هایی هستن که این حکومت علیه مردم خودش مرتکب می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/news_hut/72949" target="_blank">📅 17:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72948">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=Xi900sIROCts0wQ6bTXmc9bFIRfYBadZdz-1QzFwr2VRH9ffaW13-6iHhPKeA14_NS9roOQZPuqQ1kU9dppzChnrQ_OLEtnNZw9-1LsPpWGp7zbG9EM99_KDrN8cc9CuyOMGz4Yz2m-98pG2RMvEhApoDwLK4TDCDcbxd7SiZdJeooB_HWAnaVB_SYvx2ic8a_trgy6TIsq9hBUqj16bB90Cxdp5abRc4flioKZ2XtlKo3dTHn4fl9aJTZ3822vUVtE9ToUXsCa68lRf0uT2OzJoJ96q6mCQto5L6YTNcVQgoXv5W4dZMFHA9EBQtSaicBAwjVDeKM0TvpRFaiZB_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=Xi900sIROCts0wQ6bTXmc9bFIRfYBadZdz-1QzFwr2VRH9ffaW13-6iHhPKeA14_NS9roOQZPuqQ1kU9dppzChnrQ_OLEtnNZw9-1LsPpWGp7zbG9EM99_KDrN8cc9CuyOMGz4Yz2m-98pG2RMvEhApoDwLK4TDCDcbxd7SiZdJeooB_HWAnaVB_SYvx2ic8a_trgy6TIsq9hBUqj16bB90Cxdp5abRc4flioKZ2XtlKo3dTHn4fl9aJTZ3822vUVtE9ToUXsCa68lRf0uT2OzJoJ96q6mCQto5L6YTNcVQgoXv5W4dZMFHA9EBQtSaicBAwjVDeKM0TvpRFaiZB_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنج اصل عدالت اجتماعی شاهنشاه آریامهر برای ایران:
1- غذا برای همه
2- سقف بالای سر همه
3- آموزش رایگان برای همه
4- درمان رایگان برای همه
5- اشتغال برای همه
@News_Hut</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/news_hut/72948" target="_blank">📅 17:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72947">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=u4Xug5hvYeZDgbUz5l2MWa8qkaKsCObjvlzw3Q05nwT5kjG3Hu4P9RK5dcKpc0GAPtNl9pD8fb-jM7Xt_NHnATvonJFDWVCXbrXcZISMitDj25Ycj_bK4P6w4V2sYUcRsAV9eiY3RBDl7YD6tmWIsTHbt3BIGd72ZTQvx0klSeedBsgorpGbl_Lg0sbAeiPTeHN2W9lb8K4NOpTDq1gRqUZobCB4O0eXn5GB1tCSRUn0XOhHwJ4fse7g8Cbu6qggkejOyCPs_kNK9hd_GBF5VLZ0YtFww581liFUy3Yf7QEzIie6lCdP83n3dyo7iPSu30oExN5yWWIlZCqpM7xZ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=u4Xug5hvYeZDgbUz5l2MWa8qkaKsCObjvlzw3Q05nwT5kjG3Hu4P9RK5dcKpc0GAPtNl9pD8fb-jM7Xt_NHnATvonJFDWVCXbrXcZISMitDj25Ycj_bK4P6w4V2sYUcRsAV9eiY3RBDl7YD6tmWIsTHbt3BIGd72ZTQvx0klSeedBsgorpGbl_Lg0sbAeiPTeHN2W9lb8K4NOpTDq1gRqUZobCB4O0eXn5GB1tCSRUn0XOhHwJ4fse7g8Cbu6qggkejOyCPs_kNK9hd_GBF5VLZ0YtFww581liFUy3Yf7QEzIie6lCdP83n3dyo7iPSu30oExN5yWWIlZCqpM7xZ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر جوگیر شد و می‌خواست جلوی چند تا دختر خودی نشون بده که این شکلی بگا رفت:
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/72947" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72946">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=kE8wZTq0Q3Tf6DbjsEur9cQJgszd_XfStTl4-zTqTW8isL44Y4tY8_K2DpRGQLQAUJ1UEafyD2MJEEHJ5kskckGcAWIGMwA1vuYkdoNy-zOYfeYVcMDrXHZw9c2ZQ5oI712yDmJVaxpQsJtVOKPnCBpBkXzIGF5wJb9zSQ4jFXgRZlLrnQg14mRkgEF8IVGsw8K2kWIJvZrxa9pBrxiZFoSS4ZaoYbUsxjXj0matAtkWdm5mD3A-BELH_XMy9_fnd3gfTKXrVG4KuYsuOSyWsz87UQUYPF_S7HJE2Ip8y6EAiu8LvfRE_4mtbke42TMpL4rXHLbSqE1vx2rgSUvbMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=kE8wZTq0Q3Tf6DbjsEur9cQJgszd_XfStTl4-zTqTW8isL44Y4tY8_K2DpRGQLQAUJ1UEafyD2MJEEHJ5kskckGcAWIGMwA1vuYkdoNy-zOYfeYVcMDrXHZw9c2ZQ5oI712yDmJVaxpQsJtVOKPnCBpBkXzIGF5wJb9zSQ4jFXgRZlLrnQg14mRkgEF8IVGsw8K2kWIJvZrxa9pBrxiZFoSS4ZaoYbUsxjXj0matAtkWdm5mD3A-BELH_XMy9_fnd3gfTKXrVG4KuYsuOSyWsz87UQUYPF_S7HJE2Ip8y6EAiu8LvfRE_4mtbke42TMpL4rXHLbSqE1vx2rgSUvbMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو گرگان یه دختر 19 ساله میخواسته خودکشی کنه که اینطوری نجاتش میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/72946" target="_blank">📅 15:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72945">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=H3Jo9OXE1HKkQ0W54JSqE557_qhAgXgj8rV-_Ww-xICtqLsaFk5c9pkJ_95cZFvzEDr9c_gjktMyyj25TyTAD1VDE3Ab1Wqo3R2fcpAHrUJ17cZ2r6jyv4qCOBgNmI5WmPp2PKOk2fJBFDoODoRdJcRtMA5_yXQ9URXELbXMVRsy52yApMw4JMLbWKFfiYBSuYcetaxjkkyezzNCg_YzT_AHM4L6UAr6RiB0TbgkQWaPR7ROw2V05XXKxB4xy8W-a5Yf7qavazCUEQVnQlMqsy8JaSPioXyGAo1aNEpgJBhKl7Y-RMopB8_a5jXGU_2FlcrdTj2gwo-cmbhfm6WGig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=H3Jo9OXE1HKkQ0W54JSqE557_qhAgXgj8rV-_Ww-xICtqLsaFk5c9pkJ_95cZFvzEDr9c_gjktMyyj25TyTAD1VDE3Ab1Wqo3R2fcpAHrUJ17cZ2r6jyv4qCOBgNmI5WmPp2PKOk2fJBFDoODoRdJcRtMA5_yXQ9URXELbXMVRsy52yApMw4JMLbWKFfiYBSuYcetaxjkkyezzNCg_YzT_AHM4L6UAr6RiB0TbgkQWaPR7ROw2V05XXKxB4xy8W-a5Yf7qavazCUEQVnQlMqsy8JaSPioXyGAo1aNEpgJBhKl7Y-RMopB8_a5jXGU_2FlcrdTj2gwo-cmbhfm6WGig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هیچ کاری نیست که بخوایم یا لازم باشه در قبال ایران انجام بدیم و
هنوز نتونیم انجامش بدیم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/72945" target="_blank">📅 15:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72944">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=GnQxJMUvzDPzldeCxliodX_tDNEgFvDxAnudIfWsRVW8ab8DKYjMJpyAsTgmlOgfS3O7ODjRmjo8aOm2kZeGgLCT5NVzegdZjd41SWgyp6Gm3fXWr2FJq3tWLEbn9hBikJewi_vBqopC1UwAp6yj3YIuI-U_7niE1YnHVWXUqtOkH5g2jQM_WI5cvJc87gG8fz5VW3NSxGCVPtm3RS7GnLYEUPCGPC_lzcEgikpVLN1jpdb_TAVQp1Fz66GrXakRPtOyrz_72--pUdkxY0htOfJpOlriV95CGQm-fOkqi_zXTYpK3OKxAC2pbn6Pq_Edt2bDXrIyXC1ZySs9Wv1Dyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=GnQxJMUvzDPzldeCxliodX_tDNEgFvDxAnudIfWsRVW8ab8DKYjMJpyAsTgmlOgfS3O7ODjRmjo8aOm2kZeGgLCT5NVzegdZjd41SWgyp6Gm3fXWr2FJq3tWLEbn9hBikJewi_vBqopC1UwAp6yj3YIuI-U_7niE1YnHVWXUqtOkH5g2jQM_WI5cvJc87gG8fz5VW3NSxGCVPtm3RS7GnLYEUPCGPC_lzcEgikpVLN1jpdb_TAVQp1Fz66GrXakRPtOyrz_72--pUdkxY0htOfJpOlriV95CGQm-fOkqi_zXTYpK3OKxAC2pbn6Pq_Edt2bDXrIyXC1ZySs9Wv1Dyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
«روند مذاکرات همچنان ادامه داره و پیام‌ها از طریق میانجی‌ها رد و بدل می‌شن.
ما پیشنهاد خودمون رو که اسمش رو «طرح هفت‌روزه» گذاشتیم ارائه دادیم و دیدگاه طرف آمریکایی درباره این پیشنهاد رو هم شنیدیم.
الان داریم نظرات آمریکایی‌ها رو بررسی می‌کنیم و فکر می‌کنم طی چند روز آینده پاسخ خودمون رو ارائه بدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/72944" target="_blank">📅 15:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72943">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612c679392.mp4?token=p7sBWluIFQfT96cGehuekcpxuGwzj3Rwd50o2cNgYCL8cylV-mEXlZXppaw1B2spBxBxLBNe2m0f7yuLI2FfOobcUwYEl-iVK-4ze8jaJeaaGw7WDZUvimkvUcMx4lnZ8nHoY8483FQjLGXPgJ3z5vJIzmEbIh1hs2ic-XN4Mq1tk1_TtFwQUK9vCSmzreX1Knj15Hjxcdmihmepb-GtoS7IliEzgH75b8pt_N_Y128vIm1whn7fPXUEXFtkzTGgjkB_UGdbLV14CT_cGYzI20SU3pb92XGdJKOSigKVPw0JIl6EvbrWeUIj20VhgUZR6AsIztl8ajFrWvqAa0-QZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612c679392.mp4?token=p7sBWluIFQfT96cGehuekcpxuGwzj3Rwd50o2cNgYCL8cylV-mEXlZXppaw1B2spBxBxLBNe2m0f7yuLI2FfOobcUwYEl-iVK-4ze8jaJeaaGw7WDZUvimkvUcMx4lnZ8nHoY8483FQjLGXPgJ3z5vJIzmEbIh1hs2ic-XN4Mq1tk1_TtFwQUK9vCSmzreX1Knj15Hjxcdmihmepb-GtoS7IliEzgH75b8pt_N_Y128vIm1whn7fPXUEXFtkzTGgjkB_UGdbLV14CT_cGYzI20SU3pb92XGdJKOSigKVPw0JIl6EvbrWeUIj20VhgUZR6AsIztl8ajFrWvqAa0-QZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک جت جنگنده F-16 نیروی هوایی ایالات متحده که در حال سوخت‌گیری توسط یک هواپیمای تانکر سوخترسان KC-135 در جریان انجام ماموریتی در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/72943" target="_blank">📅 15:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72942">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=neXfrLw_EMiaKNBqBes1BywG-Ivh1Cd1MmxR68QRwptHo5Bz_6gWTU0aYO5f5AfXesXeQWtWnFTbVVZISNEdUNv9_sXN97UgowSTVl-LhW2NVRir6JSpQScMkdxyBuSGOKcCbflqut0nDveBX0bx9SXPlqWroUSladEv8uafnTCEfCSVbtYybd_s8FrxefcddQb1OiE3dscRRUYcczJZGRFmiqOFdjLW1UXpFbm7_C7IQT_duH5_lsv2U1Nkto9SJ5tIP4g6tMK9EZjOlKglmKZADLjVZ785CO2fvMoB-16KZ0-uKSlsS03i97NoUOyYOVjfV3QQeqiUjJ392wfEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=neXfrLw_EMiaKNBqBes1BywG-Ivh1Cd1MmxR68QRwptHo5Bz_6gWTU0aYO5f5AfXesXeQWtWnFTbVVZISNEdUNv9_sXN97UgowSTVl-LhW2NVRir6JSpQScMkdxyBuSGOKcCbflqut0nDveBX0bx9SXPlqWroUSladEv8uafnTCEfCSVbtYybd_s8FrxefcddQb1OiE3dscRRUYcczJZGRFmiqOFdjLW1UXpFbm7_C7IQT_duH5_lsv2U1Nkto9SJ5tIP4g6tMK9EZjOlKglmKZADLjVZ785CO2fvMoB-16KZ0-uKSlsS03i97NoUOyYOVjfV3QQeqiUjJ392wfEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا پسر رفته بودن بیرون که دیدن رفیقشون اونارو پیچونده و با یه دختر اومده بیرون،
این لاشیام رحم نکردن و اینطوری شرف رفیقشون رو بردن:
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/72942" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72941">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=iAFB0KOV3mbfs1jsGV4HnEjgQS3WTaVHg6gV-s4UMO2yiq_v5nIaAQKMBZNrgf6Fz8Luo4-KlL3uQciQ7oecRPLxzYVrT5h9ojHYoBQURqzyo5bkwOKmXd8OcY_g9tAiA6lX3hbJq5L5qqS1MQw4L7zxqQHEmUsch4e-nhOd9mh6GJu-547pI4-Pi4lCXyrkgcxdygdkyThEGOcWlJLNNDdbo1T1-UYgR3lmNJsFO_afQIO-fL8Hlsv71_lO2Cj8v190iECVE7zo27hP6NN-GTNi939YAMHLHBHKBfZtFOxkkPb1mMs4QdXnQp2ADpbl5gPZDOYWsCSixwDJuR479Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=iAFB0KOV3mbfs1jsGV4HnEjgQS3WTaVHg6gV-s4UMO2yiq_v5nIaAQKMBZNrgf6Fz8Luo4-KlL3uQciQ7oecRPLxzYVrT5h9ojHYoBQURqzyo5bkwOKmXd8OcY_g9tAiA6lX3hbJq5L5qqS1MQw4L7zxqQHEmUsch4e-nhOd9mh6GJu-547pI4-Pi4lCXyrkgcxdygdkyThEGOcWlJLNNDdbo1T1-UYgR3lmNJsFO_afQIO-fL8Hlsv71_lO2Cj8v190iECVE7zo27hP6NN-GTNi939YAMHLHBHKBfZtFOxkkPb1mMs4QdXnQp2ADpbl5gPZDOYWsCSixwDJuR479Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت مارکو روبیو درباره حمله و تصرف آتن در جریان لشکرکشی خشایارشا به یونان در سال ۴۸۰ پیش از میلاد:
۴۸۰ سال پیش از میلاد، در جریان لشکرکشی خشایارشا، پادشاه هخامنشی، به یونان، ارتش ایران به آتن رسید و بخش‌هایی از شهر و بناهای مقدس آن را ویران کرد.
بیشتر مردم آتن پیش از رسیدن سپاه ایران، شهر را تخلیه کرده و با کشتی به جزیره سالامیس و مناطق اطراف پناه برده بودند؛ اما گروهی از مدافعان حاضر نشدند خانه‌شان را ترک کنند.
آن‌ها در دژ سنگی آکروپولیس سنگر گرفتند تا در برابر سپاه ایران آخرین مقاومت خود را انجام دهند. مدافعان با پرتاب سنگ از فراز صخره‌ها تلاش کردند نیروهای ایرانی را عقب نگه دارند و برای چند روز در برابر بزرگ‌ترین امپراتوری‌ آن دوران مقاومت کردند.
اما سرانجام سپاه خشایارشا موفق شد آکروپولیس را تصرف کند. ایرانیان معابد و بناهای موجود در آکروپولیس را غارت و به آتش کشیدند و بخش زیادی از آن را ویران کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72941" target="_blank">📅 14:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72940">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=I6pdDuHhSu6mh2KFKouThqoiPO6UdLZSw3f5GTj4z-Kf6pD5wKn_qbIu4wngabTkxsxH96ngUNQSYGsF50cQaf7U0_8uaTUyr6WEXjYFYEzoIWYC-bSspuW_-zDJNBcwqDE-GE1_r1coCpZKj3zflaqqeOFmgzpc19ry3Dgv730ffDx5V34sIlPeMEQnwgr24xdZhLpoOM8A2ta6CmVtjNl4g8kI2Z8z_7ZNl9uc-BwB-8ebwbzReehccsZENx_RsoniUKn4aAE2PL66ZN4CkHv-woUg6PFJ6JayFVtxpqGdoTr0iAWNOqu0f4w5B9fafR6ZihceuHuciCagKux1cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=I6pdDuHhSu6mh2KFKouThqoiPO6UdLZSw3f5GTj4z-Kf6pD5wKn_qbIu4wngabTkxsxH96ngUNQSYGsF50cQaf7U0_8uaTUyr6WEXjYFYEzoIWYC-bSspuW_-zDJNBcwqDE-GE1_r1coCpZKj3zflaqqeOFmgzpc19ry3Dgv730ffDx5V34sIlPeMEQnwgr24xdZhLpoOM8A2ta6CmVtjNl4g8kI2Z8z_7ZNl9uc-BwB-8ebwbzReehccsZENx_RsoniUKn4aAE2PL66ZN4CkHv-woUg6PFJ6JayFVtxpqGdoTr0iAWNOqu0f4w5B9fafR6ZihceuHuciCagKux1cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانگیری: از سال ۹۷ تاکنون چین حاضر نشده یک بشکه نفت به صورت رسمی از ایران بخرد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72940" target="_blank">📅 13:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72939">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حمله ایران به پایگاه آمریکا در کویت؛
طبق تصاویر جدیدی که CBS منتشر کرده، ایران در روزهای ابتدایی جنگ، پایگاه آمریکا در «کمپ بوهرینگ» کویت را با موشک‌های بالستیک، پهپاد و جنگنده‌های F-5 هدف قرار داده است.
در این حملات، انفجار و آسیب به ساختمان‌ها و تجهیزات نظامی دیده می‌شود. یکی از شاهدان گفته جنگنده‌های F-5 آن‌قدر نزدیک پرواز کردند که حتی کلاه خلبان‌ها را می‌دیده.
@News_Hut
| CBS</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72939" target="_blank">📅 13:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72938">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beJQSl6F0femEvrDlXtJaohoRVWnb6URBeMn999A02yRbdEB8NfPg9rXaFZcCqVbXidTIsKAjT8Zfx-BW-dC1nBDmWnLErpJQBHZmn4rhJpAB-nWo8jd7ruzIT_UrfhyXi5NhSXzzupT3XLVzSL4SxxK81z7PDmk14VxjY14JZQUGBv4gn7EbQdzJWuPaMlI1gWlpte4wrgyysNBoVQYlP4GTaR4CT7XKsb11Q96W5oI__7-AeJRXNvsl1fWhWo5xFZZDpNAF4fUPwYROebzKABYNjZUSqFy-ufwl9f61rhIzXvxefjbbAPgcsoDxinA6w2zLXfSFL-21Ek_MZC9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72938" target="_blank">📅 12:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5lMsJOVyY_Z5BhsJqGbODVcKj-WVVb2Fk5Qecf4SmbyPGzaiDbw_e7EQWSBFfkxPD67Ys6IDcPsZgUUkmK87LS7IHbiqRewH17T2WcrAzGfDc8-WT-yY2UZKVA04jycQLQiNvf-lGLLOqSjIjdnD6pLfQL9Pqwelv6SFdF8PQP9w2q6Q36nbu3QN5WSV6tzQCiH5b949aqyAY-Jwz3yrn8oirHg8qUNr_5UcDAhWl5xreBhJX5b-n5fjQKc9KDgzCAkoGXZgyz2XFVLLY6ZiBJztsUNzbr_S4VZpiwTjJ8ffoH7CuVzf9MMu_o94NL4o62DoCWjtJy2vEg5dH7Kig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=Sf91gVAtfvHquIXzdaVzAJvn6-ngrkEzM8TjEytJM02IWtGT__JWBA09BKAHYLEqk89w1i96j_0huSB1Esc3BV5PvNsel_WrGvttkomeu04q_z7UCZmS6dGpCrlMmBCGYeWozf75RR4TmdT_TQkfjoJQkIcbUCTWSYTewYB4dVsgtLE4qNMTEVveJfwCW_qYbTD-pckrklKNuhhB7W9Xw-Ibc9QjBqZP6H7JjoJzNwrwbu9lvCEZLSlgyIh53Mrdr2PbNTEa93XZQEh4rRgAH1CqY51OQMw8Oc0wtlsTL7g1PCl4BYDdlf4SlJuTbIZtI3JzHRPut5GlEPmuCvymlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=Sf91gVAtfvHquIXzdaVzAJvn6-ngrkEzM8TjEytJM02IWtGT__JWBA09BKAHYLEqk89w1i96j_0huSB1Esc3BV5PvNsel_WrGvttkomeu04q_z7UCZmS6dGpCrlMmBCGYeWozf75RR4TmdT_TQkfjoJQkIcbUCTWSYTewYB4dVsgtLE4qNMTEVveJfwCW_qYbTD-pckrklKNuhhB7W9Xw-Ibc9QjBqZP6H7JjoJzNwrwbu9lvCEZLSlgyIh53Mrdr2PbNTEa93XZQEh4rRgAH1CqY51OQMw8Oc0wtlsTL7g1PCl4BYDdlf4SlJuTbIZtI3JzHRPut5GlEPmuCvymlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ؛ نامی که پس از بیش از ۲۵ قرن هنوز در تاریخ ایران می‌درخشد.
پادشاهی که ایران را به یکی از قدرتمندترین و سازمان‌یافته‌ترین امپراتوری‌های جهان تبدیل کرد؛ از ساخت تخت‌جمشید و گسترش راه‌ها تا سامان‌دهی نظام اداری و اقتصادی کشور.
داریوش تنها یک پادشاه نبود؛ بخشی از تاریخ و شکوه ایران بود؛ نامی که قرن‌ها گذشت، اما از یاد تاریخ پاک نشد.
امروز، به احترام مردی که نامش با شکوه ایران گره خورده است؛
یاد داریوش بزرگ گرامی باد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72936" target="_blank">📅 11:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZNqT3zCnAHZCZlVOhWUpvNwKVcJde4yicy8Sq9teemCSAtBGFwSdvTDQgm9JI0el0yH-SXGsXBMBWq1FZiKRSXus_L6Csg2gfgIyJta0l7hL5R4XmVFhBT90JUeANjDRmqWSOvxfVoDGxbmXr_s0dkDUht3qs_B44b88F107zzg_xgyDJ0Inb44J7rlp7HZHScnkzbo5jgya5v8OBkgN7hxeA7jFo3DIVjQSte8_oNRw1rgYjXyinmeNoUCp_nKYjIg1uo4d5vMA2mkMZrThAJf3WiYsSdWBT18BkH98IDNemLA5o8fdRuD0y2ya_zZmJUOIT0aNKl_gVNWUMmOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۲۴ ساعت گذشته، ۱۱۰ فروند هواپیمای نظامی در منطقه شناسایی شدند که شامل موارد زیر بود:
۱۶ فروند هواپیمای ترابری ورودی از خارج از منطقه (متشکل از ۱۱ فروند آمریکایی
۲ فروند بریتانیایی
یک فروند ایتالیایی
یک فروند آلمانی
یک فروند با مبدأ نامشخص
۱۰ فروند هواپیمای ترابری نظامی منطقه‌ای
۳۳ فروند تانکر سوخت‌رسان هوایی
۲۱ فروند هواپیمای شناسایی
۲۶ فروند هواپیمای ترابری نظامی فعال در داخل منطقه
۴ فروند بالگرد نظامی.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72933" target="_blank">📅 11:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72932">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxpJqsdZXZFO006EBnF1onCpH6tiLAR4B4IGxhdsAmQzQXv4zaoCIya69wcuCI7YjxK-_MxoLq_57a_K9dk4RvtAgCu4cZGF8UEJ-hHQl6va0IjBhfU9jSchwHGfuywiDF7IY5LPN8WGfPRNzIc4Dz4mAkTseKM597BR333fEkDfl-DmtLyJlGvkzq7sIZQdChgUBiN56kVUIvAJukIoAUa2taaGbs1geL9EE5jWJ3gskZBuvfvWsz1jFBe0i4Y5Bj0j_AhcgPabP4nhBZ0AmOV_cE6_l3sQOciCFKoeKJ-a9utk1m7rbQ31-TaU_8UO_ZQeyd797LbcIBHa63d45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
پنتاگون به ارتش آمریکا گفته خودش رو برای حملات احتمالی دوباره به ایران آماده کنه:
طبق این گزارش، هنوز دستور نهایی حمله صادر نشده و ترامپ همچنان درباره زمان و اصل حمله تصمیم‌گیری می‌کنه.
اگه حمله انجام بشه، احتمالاً اهدافی مثل تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران مورد حمله قرار می‌گیرن.
منابع آمریکایی و اسرائیلی می‌گن احتمال انجام عملیات قبل از انتخابات آمریکا و اسرائیل مطرحه.
همزمان، تیم امنیت ملی ترامپ درباره جنگ جلسه داشته و ترامپ هم طی چند روز اخیر دو بار با نتانیاهو تلفنی صحبت کرده.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72932" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72931">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72931" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72930">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAltVedgwGwjxTXKpJkDoF2TdRMnP0_SWxxxRce2Ae3iU-8hvE3GcCneAQZHTPva7aVfhOHLa5w-BMGT3uiY01A82kEGu4xZJIgu6OdgDhfpEytgfZpm75jichP94umCsUr_LHd1t7R0DJ-sgCoPCZf2_-536pqKwgApwSjKGyIOUiBKXpZ7Tm7haMObv-DZPUxsbDi5YTWWoAKeA8cnOC_ddf5opoj_eIGwy9T3dmUEv6EEo5BStF5HVmqFb9j-rXkUq_GhnXaeaeWlbPGaI2i8b8iE5pwwjAKuSNEXBnCEqlkTxDlwmnN6fNcmOk5NO5uwq7lvUoqY_Ix5Elt6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تراکتور
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
⚽️
تراکتور: ۳ برد، ۱ تساوی، ۱ شکست و ۶ گل زده
⚽️
استقلال: ۱ برد، ۳ تساوی، ۱ شکست و ۳ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72930" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72929">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=kQo9MWsh_eq_JeHufTnWCej2RiTFsBccjhG060m1SBAHbv5-Hds2wAqEBs6Cl-tbzzHxyKiEp4UxOMntdCCFMEq3MQf_8ZSI5nnp1zviAVJUzi6oh_wc8wyLqoCeKkYchOWOy_Odx6bg6JxMe2hUZzc2xnO-EL0hKiJpVDfYcvHtspFPqFGpEmPvKB4rW5BAsNjAFD2Ku-Hby_dRC7wHAGZjXNJFOhN6PEdtmoL3eaoaszdKYbQdBsBDtkTrRRNMijjq1lalsliyoWVSFj9sbtF222LdNQwXcvVsVgY2OaiPYZ-gWxZcNL2SziqMG1rDeX80Vw9-8PnkVHfIc_GesQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=kQo9MWsh_eq_JeHufTnWCej2RiTFsBccjhG060m1SBAHbv5-Hds2wAqEBs6Cl-tbzzHxyKiEp4UxOMntdCCFMEq3MQf_8ZSI5nnp1zviAVJUzi6oh_wc8wyLqoCeKkYchOWOy_Odx6bg6JxMe2hUZzc2xnO-EL0hKiJpVDfYcvHtspFPqFGpEmPvKB4rW5BAsNjAFD2Ku-Hby_dRC7wHAGZjXNJFOhN6PEdtmoL3eaoaszdKYbQdBsBDtkTrRRNMijjq1lalsliyoWVSFj9sbtF222LdNQwXcvVsVgY2OaiPYZ-gWxZcNL2SziqMG1rDeX80Vw9-8PnkVHfIc_GesQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یه هموطن گفتن که این خونه جن داره، اونم خیلی پرقدرت و باشکوه وارد شد،
اما خروج جالبی نداشت:
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72929" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72928">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=UKQ7zUyXhvhyTTnogLgilnxA0mAQBliliZc2LX97PihurARaSKiw7pT4KavTscOsBTacHdOSxxi_KAxIG_6CrZma7F6bTfbC4YmHuRUx3A1W1n4NRJZuatbP7l7_uMMhf2lSSNH5JnvlJwLdXIcSLZO2E85qhm2L04-1Ogm_iVc2FQa861GfgwdLqqVyXy68yuag4-PhPVgJIJ7y0LEoEDPwy8B5Iq_cm9JwTCNy70F7HaXIrXFdgfzzoL96cVsT5ny30s1bHD8JKa2yWaGf6LtsIsu8zbiYRD7dEzn8KjW9NiHGrbGaPxTrdSokUijjtKuHtnVMe9htiFs1ryNERA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=UKQ7zUyXhvhyTTnogLgilnxA0mAQBliliZc2LX97PihurARaSKiw7pT4KavTscOsBTacHdOSxxi_KAxIG_6CrZma7F6bTfbC4YmHuRUx3A1W1n4NRJZuatbP7l7_uMMhf2lSSNH5JnvlJwLdXIcSLZO2E85qhm2L04-1Ogm_iVc2FQa861GfgwdLqqVyXy68yuag4-PhPVgJIJ7y0LEoEDPwy8B5Iq_cm9JwTCNy70F7HaXIrXFdgfzzoL96cVsT5ny30s1bHD8JKa2yWaGf6LtsIsu8zbiYRD7dEzn8KjW9NiHGrbGaPxTrdSokUijjtKuHtnVMe9htiFs1ryNERA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«استیو ویتکاف داره روی توافق با ایران کار می‌کنه و خیلی هم خوب پیش می‌ره.
فکر می‌کنم این توافق واقعاً چیزی نیست که بخوام انجامش بدم، اما ایرانی‌ها حاضرن برای اینکه این وضعیت متوقف بشه،
هر چیزی که ازشون بخوایم پیشنهاد بدن.
»
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72928" target="_blank">📅 10:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72927">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ درباره ایران:
«همون‌طور که قول داده بودم، دارم مطمئن می‌شم که ایران هیچ‌وقت به سلاح هسته‌ای دست پیدا نکنه. خودشون هم اینو می‌دونن.
به‌زودی از اونجا خارج می‌شیم و می‌بینید که قیمت نفت مثل سنگ سقوط می‌کنه و قیمت همه‌چیز هم پایین میاد.
این عملیات بزرگی بود که رئیس‌جمهورهای قبلی باید سال‌ها پیش انجامش می‌دادن. باید انجام می‌شد، ولی هیچ‌کس حاضر نبود زیر بارش بره. ما چاره‌ای نداشتیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72927" target="_blank">📅 10:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72925">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=WmbdRiXORsZpLnaHMhJthHDB_zkD2lAl_sL6XP-3YQQbFytGk-6AYwHUWB2Q3cRgtZpCV_HPixJsuwbsv7cq39-HTklZIfQCOydSduvzGEObJ21caBldXJZfuHC_TB7FaK3z3ag_iM1AIy_qZ684lOrwCQ2b8PZ55SS3lmSPLGls0wWlq_vuo98hsUzcB8H989pFh7cYHRiytwqrfJnEfiDcTopZogipwgnzZ5__pzg8Mqy2W220o5mwwFp0p9Lu7GzpiajRI2ZdjQMJDGlmTJowPlps8c352odU0vJ0Y2vr1IX3ughk9zTVW5XggFfJFhck_4Tp41O_3rj0h8OdEDXhYKShJaZzgV_AhPJxBrfFHGFqlDfJCLRvBFxCnOFaWfutz8_lBa-gMDWLkiMelDjxc0vsfOWc_NgwMxNnBAJYCMbsfzvx0l5GRY4FXorlxJ-4zFaGS0PxVHy7XMoVbo_B7mfNq9mV1wzo7sGzKTh5mksVNpAzogy4pysomef73XRb4v4LTVqPnNesudVyCR_FBao6H3DIWRpohh31dUToTZVX_G74SK_l4oS9dAsu2PcPs_qLcC9h7ichyEChSeSRIkqOSBEChBTBdFlrTF9nrY9kefBTZUHv0wU0RcGvLRUAbT1n92tNTTlj7ZdhURFgtlBi4yYMsT_Obh06EXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=WmbdRiXORsZpLnaHMhJthHDB_zkD2lAl_sL6XP-3YQQbFytGk-6AYwHUWB2Q3cRgtZpCV_HPixJsuwbsv7cq39-HTklZIfQCOydSduvzGEObJ21caBldXJZfuHC_TB7FaK3z3ag_iM1AIy_qZ684lOrwCQ2b8PZ55SS3lmSPLGls0wWlq_vuo98hsUzcB8H989pFh7cYHRiytwqrfJnEfiDcTopZogipwgnzZ5__pzg8Mqy2W220o5mwwFp0p9Lu7GzpiajRI2ZdjQMJDGlmTJowPlps8c352odU0vJ0Y2vr1IX3ughk9zTVW5XggFfJFhck_4Tp41O_3rj0h8OdEDXhYKShJaZzgV_AhPJxBrfFHGFqlDfJCLRvBFxCnOFaWfutz8_lBa-gMDWLkiMelDjxc0vsfOWc_NgwMxNnBAJYCMbsfzvx0l5GRY4FXorlxJ-4zFaGS0PxVHy7XMoVbo_B7mfNq9mV1wzo7sGzKTh5mksVNpAzogy4pysomef73XRb4v4LTVqPnNesudVyCR_FBao6H3DIWRpohh31dUToTZVX_G74SK_l4oS9dAsu2PcPs_qLcC9h7ichyEChSeSRIkqOSBEChBTBdFlrTF9nrY9kefBTZUHv0wU0RcGvLRUAbT1n92tNTTlj7ZdhURFgtlBi4yYMsT_Obh06EXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از مدرسه دخترونه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72925" target="_blank">📅 09:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=GavkoFeeMIljhECQ7pCrrb8i98BW9zfO6TgpdSYvUjS_zAyFKxWrKTijVoxAax4tt1tUtHBPeqLuaEaGkTWtBoJ3o3zTz13SGv5ZUx-V2v2SNV4V5dzgwPPbi_k6n3MC82PMLackojY1OADA3BXOo_tt2zp_wmScXp8oYK519WxsI8KmFbbt1Uk9gzQ6G_U7gw0XHYdDPEcN6zxSc96iQfz8tPk8mijGjPW4YEEOlfxsDqrVxZJqzU1aXC5cU4I_teih_KAT9bBcRMmPQMxRu29tx9Foe2FQW-rMl4_6AhKStIKl682fm3suDlcJv1-j1gXixw1JMpbYM74C0WI5hFiHBNJePhku_3BeBjUOlIl6JExHu_69AqTc2EXjg8uQLfk4AJjokDGekE0g2rbocUxTDr_auavTmqMd3ZIYF-puLOxkzUMUn08WwHQFUKuyZfxObLH-OkBAoXWQuYinu1MmaOJcB7LOtEHghoMUwBd9DPgUCqtnQulXkC0lsCVlwXBZcnvbybyBzHGqoJVZhcL5X5P4rAgmc0FBHJlkcJSz0WFeS4DcXb7QpgA582xnweBy-74PsnkrjQqATM4xEIJCD1nH6B9hzWdAfmiwMmFbU7cwhg1SYYiO2atKGPXF7-gNtgzHpTn-qaA3SlrzT3o5K0NzaZpuSW1FhFeT3vY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=GavkoFeeMIljhECQ7pCrrb8i98BW9zfO6TgpdSYvUjS_zAyFKxWrKTijVoxAax4tt1tUtHBPeqLuaEaGkTWtBoJ3o3zTz13SGv5ZUx-V2v2SNV4V5dzgwPPbi_k6n3MC82PMLackojY1OADA3BXOo_tt2zp_wmScXp8oYK519WxsI8KmFbbt1Uk9gzQ6G_U7gw0XHYdDPEcN6zxSc96iQfz8tPk8mijGjPW4YEEOlfxsDqrVxZJqzU1aXC5cU4I_teih_KAT9bBcRMmPQMxRu29tx9Foe2FQW-rMl4_6AhKStIKl682fm3suDlcJv1-j1gXixw1JMpbYM74C0WI5hFiHBNJePhku_3BeBjUOlIl6JExHu_69AqTc2EXjg8uQLfk4AJjokDGekE0g2rbocUxTDr_auavTmqMd3ZIYF-puLOxkzUMUn08WwHQFUKuyZfxObLH-OkBAoXWQuYinu1MmaOJcB7LOtEHghoMUwBd9DPgUCqtnQulXkC0lsCVlwXBZcnvbybyBzHGqoJVZhcL5X5P4rAgmc0FBHJlkcJSz0WFeS4DcXb7QpgA582xnweBy-74PsnkrjQqATM4xEIJCD1nH6B9hzWdAfmiwMmFbU7cwhg1SYYiO2atKGPXF7-gNtgzHpTn-qaA3SlrzT3o5K0NzaZpuSW1FhFeT3vY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو تهران، عده‌ای ساعت 9 صبح از خونه زدن بیرون، کفن پوشیدن، به سمت قوه‌قضائیه رفتن و به پسر پزشکیان لعنت فرستادن :
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72924" target="_blank">📅 09:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72923" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72922">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72922" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAwcLmWNg_2EoaLprX2Ub-8QmrD5YLVkcSDSY1oYvs0WstHfalIl0YBhO_uvWN1MQTOTKKe50ouahWfzad4HFlEE3TEIturERCQE8cTb7a8ZCzYzA1FTSMTTWU-q3G6u-z7rIHY-I7bjSmXbHxuamvvyizpohytz0PWHJH5-IbmmoSdzIbTZMz64GAAVwyfAAwbEkiH27RKnpU-ti0p4TfInzuYY64151OiAS5bhUozIWdTKrVcbNWWsmnWChrSmsLwVNnXs9nWxpcyFeCcnbHM6LjmdfAtcCYm50Z90zOVzOOiA_FpGZvsfz-praSpS7OUmriFd590XILtbOnGhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ce4yhSfQTZ_wOkokYX2_MKq7S0MHreG8bO8k9uXq3NXetAfuIZIsenVotqscldQ0WkHyqIZF9Z-Ju2MOi9pC0xv8f3dEM18YkzpFEl1nqQrD2xCc-7X-VrIERg0QjYCX0o2i1ogSusX_Ke-38qUyVrGwsdADJ_QWDfjRC_jyafL9bPASjzcVmFeobBxkreKDUfOtyqYfBKA6D-E_8WBUb47FXMctWJC4iY-736r8X3m4dabL_cEeIgy87VPqyLeXX94kPO6r0Es5HpALOduB9zWHcRoYx5WY5tA9OmLvyzyPv7xhm6ETqJnMiNylm0eioajpmoT26379JKr3ImwIsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=TFqQJi_dbAJTzrNZBlBY5jmxdUvquYI-AVCff7RYgehAEjfa1b8ACJVqOWEgDj9jr2HkBO0epgO2_Ey7VTKd2WPi_bJ557G3uAZhkyBQKU1h3nYSXZ5UFoN0yOlGS4fUnKcIldXs3nEpaqghyx3uiSRcbxPmw_9msyy4FL6aUmJvIT6g1kTuuEdFAuWyhNXZmAjCUXJzDIljV1X637BMbG9aPo33HJH5HUKK1oMxMj9wRgb239e5Edjm9lIvLcJVv45B9afDaXyRJaVtLIgTyfNw4qkv-c6XfSPI-EYsRe4f3ftDE_KlpNe20OfkhRKauThARQxmauK_PN0do4ScLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=TFqQJi_dbAJTzrNZBlBY5jmxdUvquYI-AVCff7RYgehAEjfa1b8ACJVqOWEgDj9jr2HkBO0epgO2_Ey7VTKd2WPi_bJ557G3uAZhkyBQKU1h3nYSXZ5UFoN0yOlGS4fUnKcIldXs3nEpaqghyx3uiSRcbxPmw_9msyy4FL6aUmJvIT6g1kTuuEdFAuWyhNXZmAjCUXJzDIljV1X637BMbG9aPo33HJH5HUKK1oMxMj9wRgb239e5Edjm9lIvLcJVv45B9afDaXyRJaVtLIgTyfNw4qkv-c6XfSPI-EYsRe4f3ftDE_KlpNe20OfkhRKauThARQxmauK_PN0do4ScLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۷اکتبر ۲۰۲۶؛ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس رونالد ریگان» (CVN 76) در حال ترک سن‌دیگو:
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72919" target="_blank">📅 01:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=qqTLkyzE4qxDKw1VnB6-pp7WClL_zLgw9ZAe7d0VQTjQFvsnEuUxiBJt5Jc6ZmKddOjha-nwl7A5xg4aJ_f9H8k4CJew1roMCMEdTS1kZagzq2kkP5aH0yp03R_W1ZNQ_8fDKsREbh9GiWi9qEseYN6kEeR9sQ5E09eIAHtg1SMXW8QdE3umqtIodkMVv4VEfbcZSMSssKU-e6Nf-NF-lX_QXTJ8hlQ3yszdBtW7bgV7AwzQpK8TtIM2MKdqK_aVzorqeYgSX6d8JlIrm20Kk_ep6srR2K8ICoGJrlY76r6AWyDXOO3DNgImchmzUMlxqBQw6XhrmWRgSKHy99z_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=qqTLkyzE4qxDKw1VnB6-pp7WClL_zLgw9ZAe7d0VQTjQFvsnEuUxiBJt5Jc6ZmKddOjha-nwl7A5xg4aJ_f9H8k4CJew1roMCMEdTS1kZagzq2kkP5aH0yp03R_W1ZNQ_8fDKsREbh9GiWi9qEseYN6kEeR9sQ5E09eIAHtg1SMXW8QdE3umqtIodkMVv4VEfbcZSMSssKU-e6Nf-NF-lX_QXTJ8hlQ3yszdBtW7bgV7AwzQpK8TtIM2MKdqK_aVzorqeYgSX6d8JlIrm20Kk_ep6srR2K8ICoGJrlY76r6AWyDXOO3DNgImchmzUMlxqBQw6XhrmWRgSKHy99z_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72918" target="_blank">📅 00:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cltm3qSiiOYcxn0adXXGFmiwH24BWwywynBySVwyk9N_NghCZzCkNjq_-a8hjYGfh58t9HkSHN3410QNm5IFh1HmXoszaLeJokaZIht9CyTKQc88QQARLTo2XTNY7qY-32qIywTPcO32ncqUHs97WCF81Y6eaaOsjIIHAVfKyBcI3RBSGBYBJhM8xpNGNVLaRvqmtsK-WFxWo7OA3r-mTiMQUl-3J5KP3kJnHFWCcPUlZsF6JDynQ705URKmVJl_ZN30NREQB_cVmVLzNLY02nYBwv0DwCELfad-k6G2kE9_pBd2FHAEY_j2QF2olhDV_I1NG9py2jCIGFFF5lxryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: کاخ سفید از پنتاگون خواسته گزینه‌های حملات جدید آمریکا به ایران رو پیش از انتخابات میان‌دوره‌ای ۳ نوامبر آماده کنه؛ البته هنوز هیچ تصمیم نهایی‌ای گرفته نشده.
به گفته مقام‌های آمریکایی، ترامپ می‌خواد قبل از انتخابات نشون بده که در جنگ پیشرفت حاصل شده و هم‌زمان به کاهش قیمت بنزین کمک کنه.
همچنین گزینه‌های اقدامات نظامی گسترده‌تر برای بعد از انتخابات میان‌دوره‌ای هم در حال بررسیه.
@News_Hut
| The Atlantic</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72917" target="_blank">📅 00:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=ZPGcHET2Zt7O-hX5djfZbo1X1lHoIdrtvdzi8WjmijC9_mOXDY5ctIE_mE80_aMXdEme5ih6a1g1Q6DdtHPtzUGpnzMzIc7-KfHEJnn2YEV97jU5M1y67gDwgHuxd76hGAVISzmODo8fWJFN9zrVWm_7OMZPVHaVQ9LR8WmaT-EGqXgzK2L4TI4F_RftjkF9L4iYgH-79ecRH_1_DsBBoxOJkLSZl97lVNUTP7H4suNwe7xOVeFqp4i83RXwfmcZValRKHXVzKlv0E4wD1IU_rTfd-FnPGI1SIrgCW7QJZ53YXM0aoyih1-aBwNYhcXxUaqBNMUD2J9TQVTctGziCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=ZPGcHET2Zt7O-hX5djfZbo1X1lHoIdrtvdzi8WjmijC9_mOXDY5ctIE_mE80_aMXdEme5ih6a1g1Q6DdtHPtzUGpnzMzIc7-KfHEJnn2YEV97jU5M1y67gDwgHuxd76hGAVISzmODo8fWJFN9zrVWm_7OMZPVHaVQ9LR8WmaT-EGqXgzK2L4TI4F_RftjkF9L4iYgH-79ecRH_1_DsBBoxOJkLSZl97lVNUTP7H4suNwe7xOVeFqp4i83RXwfmcZValRKHXVzKlv0E4wD1IU_rTfd-FnPGI1SIrgCW7QJZ53YXM0aoyih1-aBwNYhcXxUaqBNMUD2J9TQVTctGziCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72916" target="_blank">📅 00:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=KC_5PJ9wckTo1yWl8jhaU6q2CfoT3tXK5i6td-PsREDPRFQ7FLChR9QYPWhv6NWrS08dqDGMbdeBQj2FxvNC6RsYMAA1aa91jCzvanF0Iaay4NgttvpEsQtqNUt_et68n6ym9hVDGLP-0PmABTNmUrkqtaI5sTNnXOcHSVZ6mx-z64GXQ1HYLuBWJJq8l0oE68_J01ImkD-2vxwWC5U5rK0F6pNBBdWBmurl3n-EGPuUd7YT7x8Hrt2XngkBpyUP_K0i8kSaS5TQSNZoDXciSiwP2XkDmTyimbL9pqw8u0gKCTNb1l2iLrWdGdG2VrAoub4F0pJcWHFR9t124OThog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=KC_5PJ9wckTo1yWl8jhaU6q2CfoT3tXK5i6td-PsREDPRFQ7FLChR9QYPWhv6NWrS08dqDGMbdeBQj2FxvNC6RsYMAA1aa91jCzvanF0Iaay4NgttvpEsQtqNUt_et68n6ym9hVDGLP-0PmABTNmUrkqtaI5sTNnXOcHSVZ6mx-z64GXQ1HYLuBWJJq8l0oE68_J01ImkD-2vxwWC5U5rK0F6pNBBdWBmurl3n-EGPuUd7YT7x8Hrt2XngkBpyUP_K0i8kSaS5TQSNZoDXciSiwP2XkDmTyimbL9pqw8u0gKCTNb1l2iLrWdGdG2VrAoub4F0pJcWHFR9t124OThog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله سرحدی، مقام طالبان:
زنان بی‌عقل هستند. آن‌ها از نظر عقلی ناقص‌اند.
آن‌ها هیچ‌چیز نمی‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72915" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=QkXOFbYqrb6H5-idxQ9FSWgiFZ8uAY5Zo-E5eRrnNjqHCs50CGR_sBC3_URUJL2KqNQ6ZZs2lTXmkq0NJvX4lJS7itBx95yq6S9LtEH_S-DHAaGwSrjipOgDTsI8dUISpg3pEAIK5_LlDwzeP5k-KjR2L17hYPzq2vlBI7ztxj9EiuZxAYzhaFfbei2jzFmRkONk3lImFq-XgRwPYbN-RR9txLml-uReOQKuWslc5vCva8__GblDDv-ykY74DE2LL02XVF7o9xManrze8cRWPgHeM95_wBdCdXdG1vfaN2mJoQyRBc9uJW99l2iLXQhzthVthHs7rj6yA_K646KFfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=QkXOFbYqrb6H5-idxQ9FSWgiFZ8uAY5Zo-E5eRrnNjqHCs50CGR_sBC3_URUJL2KqNQ6ZZs2lTXmkq0NJvX4lJS7itBx95yq6S9LtEH_S-DHAaGwSrjipOgDTsI8dUISpg3pEAIK5_LlDwzeP5k-KjR2L17hYPzq2vlBI7ztxj9EiuZxAYzhaFfbei2jzFmRkONk3lImFq-XgRwPYbN-RR9txLml-uReOQKuWslc5vCva8__GblDDv-ykY74DE2LL02XVF7o9xManrze8cRWPgHeM95_wBdCdXdG1vfaN2mJoQyRBc9uJW99l2iLXQhzthVthHs7rj6yA_K646KFfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگاری پرنده‌ها با این هموطن مشکل شخصی داشتن و اینطوری باهاش تسویه حساب کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72914" target="_blank">📅 23:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=P4zGKyEqdIGjHoAkHyeI8nqJbyM-Df7crWzg5XiwutiVevkcXClE2xSCpkUmYddDv8LQLyuEuLbo07R3rodBwqVRnWdf8X6ulAZVR1q8wxIU7oEsgn-5Zh-yC4S_wWg_fEJq3EFQAI_Bz53qscZZu2mYS01WFJG_wynqPLkcIh7OBKgOAcxMRtZxrocCV-940BpKMfwColdwW4Z9BOULX1oyRUnKJc2J9WVn9osLvfxsez9yQGv6eJhJWfvIgRqx1qdWL7DcrWgL5jTfssAlvhI3olkP1Dj81z2Jda4vlECIDZ976H9tr8EJ_STS8isIc0gchyw_i_VNn2UHA74cDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=P4zGKyEqdIGjHoAkHyeI8nqJbyM-Df7crWzg5XiwutiVevkcXClE2xSCpkUmYddDv8LQLyuEuLbo07R3rodBwqVRnWdf8X6ulAZVR1q8wxIU7oEsgn-5Zh-yC4S_wWg_fEJq3EFQAI_Bz53qscZZu2mYS01WFJG_wynqPLkcIh7OBKgOAcxMRtZxrocCV-940BpKMfwColdwW4Z9BOULX1oyRUnKJc2J9WVn9osLvfxsez9yQGv6eJhJWfvIgRqx1qdWL7DcrWgL5jTfssAlvhI3olkP1Dj81z2Jda4vlECIDZ976H9tr8EJ_STS8isIc0gchyw_i_VNn2UHA74cDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره 300 تجربی شده و زنگ زده به مشاوره‌اش داره گریه می‌کنه که چرا نتونسته زیر 100 بشه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72913" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=XbO-wR8OuEeeH2APx-NMb45-Pd94shXIL7f-Cew6UrR_MmleHvSVQlrGWtt39DG5lRNDYblIEXPe5bZBr2E3PuVWNhynIHw64Ui7lZpFQtBU8ElH4QXTzWR_zhnJo3sq50C-W0fL21TdmlNYwbZne7eJ_qO63QWGHWeRZBpDaqO5h1WTOjK1Ovr6XSmp2IQJ2E0cGBgt001vcZ-qdP7SUG9hrdMj0uvODJjYUpsRaj_m3dqSkYIl5NmTsN0C5Diqd5cIsrPhaoCQRolJ5Skh6tRbGMqxByNIreOMV94ECVy01miI4f3fbwXsBJehNJvq92K0ul5aGZLfNM5r9qb7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=XbO-wR8OuEeeH2APx-NMb45-Pd94shXIL7f-Cew6UrR_MmleHvSVQlrGWtt39DG5lRNDYblIEXPe5bZBr2E3PuVWNhynIHw64Ui7lZpFQtBU8ElH4QXTzWR_zhnJo3sq50C-W0fL21TdmlNYwbZne7eJ_qO63QWGHWeRZBpDaqO5h1WTOjK1Ovr6XSmp2IQJ2E0cGBgt001vcZ-qdP7SUG9hrdMj0uvODJjYUpsRaj_m3dqSkYIl5NmTsN0C5Diqd5cIsrPhaoCQRolJ5Skh6tRbGMqxByNIreOMV94ECVy01miI4f3fbwXsBJehNJvq92K0ul5aGZLfNM5r9qb7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیوپ برای استخر یک میلیارد تومان!!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72912" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=CMrahZhTqrh9S3HVxkszYBCovDcN8ninWfzgA_F2CZoX3SMCW8cf-V-77AIbDzD0GU0p0CT4UCXAMh-vMZ4DrStbwbfgmar-ZDDhQTGAHOTmgGwbrTnxxS_4yWcSrmc_A8VmgzedyDc5BxibnKxd2Cy0fHVlNAeAL2TAmWVRWNfUPfW4Ztg1Ey09BUzqf3PxxMFfd_wDe6aExTDjAkhD9oaDIwlv6R5gbdQyfPxUZsJE15pk6XwnFKeR-zpDF4KCgOob22gys7u9HGnd2qDy7BGTa3tS92bW-ZdgObG7VEwJiz7zZVSYsRsBhP9nrIqfsJ2l5cEwRhrW6WReitVOMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=CMrahZhTqrh9S3HVxkszYBCovDcN8ninWfzgA_F2CZoX3SMCW8cf-V-77AIbDzD0GU0p0CT4UCXAMh-vMZ4DrStbwbfgmar-ZDDhQTGAHOTmgGwbrTnxxS_4yWcSrmc_A8VmgzedyDc5BxibnKxd2Cy0fHVlNAeAL2TAmWVRWNfUPfW4Ztg1Ey09BUzqf3PxxMFfd_wDe6aExTDjAkhD9oaDIwlv6R5gbdQyfPxUZsJE15pk6XwnFKeR-zpDF4KCgOob22gys7u9HGnd2qDy7BGTa3tS92bW-ZdgObG7VEwJiz7zZVSYsRsBhP9nrIqfsJ2l5cEwRhrW6WReitVOMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«شاید من جلوی نابودی کامل جهان رو گرفتم، چون ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت. و این اتفاق خیلی مثبتیه.
رئیس‌جمهورهای قبلی باید این کار رو زودتر انجام می‌دادن، یا اصلاً یکی باید این کار رو انجام می‌داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72911" target="_blank">📅 21:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=TXarK36BefbFziotW7zJFh9XO86RpL7vAsSizrkVZ-md__N3F_WdKnaHMSUhj0W-Yt4quyfwMhA9Xjc2g75b4vNFyrKS02Ynf0bwOuKGXFQXgM_fvxSGHZfeY_8pc0FKoZoeCA6s6IgBlLRKzM-kCnooHvP4nSwCvow8B5DkUjApj0jqf0xWmsgofnMH30fKwDARIJ7FXH5GxkmKI9lNK5HPR1eqBlfam3i_xLn19ZnQy658iLTY0VsjTTJ3KOSDhMgpSEES55EEcsvXSN7aIodwUTt2l6OFQexZYSWnQ-ca-GsqQ9jhyHuM2LH-GksfxJZIMG5lnKKQcRLxZDv6xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=TXarK36BefbFziotW7zJFh9XO86RpL7vAsSizrkVZ-md__N3F_WdKnaHMSUhj0W-Yt4quyfwMhA9Xjc2g75b4vNFyrKS02Ynf0bwOuKGXFQXgM_fvxSGHZfeY_8pc0FKoZoeCA6s6IgBlLRKzM-kCnooHvP4nSwCvow8B5DkUjApj0jqf0xWmsgofnMH30fKwDARIJ7FXH5GxkmKI9lNK5HPR1eqBlfam3i_xLn19ZnQy658iLTY0VsjTTJ3KOSDhMgpSEES55EEcsvXSN7aIodwUTt2l6OFQexZYSWnQ-ca-GsqQ9jhyHuM2LH-GksfxJZIMG5lnKKQcRLxZDv6xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: الان از روسیه همون حسی رو می‌گیرید که اوایل کرونا از چین داشتید؟
ترامپ: «چین اون موقع خیلی چیزی نمی‌گفت و روسیه هم الان خیلی چیزی نمی‌گه. ولی روس‌ها می‌گن که اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72910" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=UyvIW6oD6BsHk9NoQhX-Hi-5Y5-xG8EX9B2tkm0t_xEG46bbLxYOZ2cc4qOfyP-isqGuSgf6D4mseWJZssq_IPg_As0PyV9v5eWM4KLyBX7Yvnz2lY4zpqAXyQFn8AeKRBT6GKMytP1fO6oQalt4Am7mbLu8-490xJQraz1A59T1IIm5VJlRpaD6LKXDuM43J-_3UeBC0vFR_NWOWXYTd22_nI2SYvHP7NAE7SpVe6S9V0aa0XmDJXVOWUOoimPlIMtMbdxtYjs2imAc1lZ8YJR5E3J7Ly83A0wFdY_iqXkXTSmpywOA1V66Q6xeN57bm6NflUTM4XI7q0WhbX0p8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=UyvIW6oD6BsHk9NoQhX-Hi-5Y5-xG8EX9B2tkm0t_xEG46bbLxYOZ2cc4qOfyP-isqGuSgf6D4mseWJZssq_IPg_As0PyV9v5eWM4KLyBX7Yvnz2lY4zpqAXyQFn8AeKRBT6GKMytP1fO6oQalt4Am7mbLu8-490xJQraz1A59T1IIm5VJlRpaD6LKXDuM43J-_3UeBC0vFR_NWOWXYTd22_nI2SYvHP7NAE7SpVe6S9V0aa0XmDJXVOWUOoimPlIMtMbdxtYjs2imAc1lZ8YJR5E3J7Ly83A0wFdY_iqXkXTSmpywOA1V66Q6xeN57bm6NflUTM4XI7q0WhbX0p8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
ترامپ: «فکر نمی‌کنیم این‌طور باشه. خیلی زود متوجه می‌شیم، اما فعلاً فکر نمی‌کنیم سلاح بیولوژیکی باشه.
روس‌ها هم می‌گن اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72909" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، در سن‌دیگو همراه با تفنگداران دریاییِ بال هوایی سوم تفنگداران دریایی در تمرینات بدنی صبحگاهی شرکت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72908" target="_blank">📅 20:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=TSEc6kDHH1SGjePxYwafufTcvuLTRed8ccrWpG7E0g3d0h23FTqrliwZvlfU5xcuAGky6tBCvEteNIfVTuYiZoNCkTLm0RadRDU5nluo0CrleYhZKsq6z_GmfIGptfqNdRW7SCC7ZfFNdvEL3U24G0hYt8YHVPhIcMOPHIOOm-CpNV9F3UcWlgvaHlH5dXD0hCrhhW_Rgy_79ijj7G_Xq6jIFn8FkFPEXH_WQYBoVR8jzAI35rrJ0erHH-Vpor9gOrx6tLW38bUD0HJqhQeX2X-ZFfZWIz1yFzqBNkVb2txVfSyZW_KKyK7bYBDnANgtp2eHcAkzSM7OCEsQiucFxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=TSEc6kDHH1SGjePxYwafufTcvuLTRed8ccrWpG7E0g3d0h23FTqrliwZvlfU5xcuAGky6tBCvEteNIfVTuYiZoNCkTLm0RadRDU5nluo0CrleYhZKsq6z_GmfIGptfqNdRW7SCC7ZfFNdvEL3U24G0hYt8YHVPhIcMOPHIOOm-CpNV9F3UcWlgvaHlH5dXD0hCrhhW_Rgy_79ijj7G_Xq6jIFn8FkFPEXH_WQYBoVR8jzAI35rrJ0erHH-Vpor9gOrx6tLW38bUD0HJqhQeX2X-ZFfZWIz1yFzqBNkVb2txVfSyZW_KKyK7bYBDnANgtp2eHcAkzSM7OCEsQiucFxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجایی که مشاهده میکنید تگزاس نیست، کوهدشت لرستانه که یه چند نفر با همدیگه به مشکل خورده بودن و تصمیم گرفتن با کلاشینکف حلش کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72907" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnKVx1Oe3izZlYP3yoRwQltbtndd8heP4hITrQu3ygsZ_j2EmccWMs44VxqHPnzeieKdRT3XLqP-fVaq2EZkor0hTrzQdrbZg8TAYkht9jpg1YeLcr2ukQfuIC5bADkLk9X7z9tFW4eLhOTD3BCbLfeBNvDy1305FYgM4Ea4ERJ5ZTHeKWORKgWe7Xy-J1OnaigxKIRob-rGT7EnwTi2_AFuoTeHa2LhEyxR0qbbaggJXW-TQtKVyaQTT3HgMx-jE-4U-jf68O_cYZCZpMTAq_PNqM1A8o95J50JVqRNoEGFJ7jt0VI4SwxIwEHbEdO5UWQFbq9WXLHn7uvW9XiwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه
!!!
طبق گفته منابع رویترز، قرار شده به هر خانواده ۳ هزار دلار پرداخت بشه.
حدود ۵۰ هزار خانواده که خونه‌هاشون تخریب شده یا از روستاهاشون امکان رفت‌وآمد وجود نداره، در اولویت قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72906" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72905">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=rq2v_dHUJTdorFwqyMBBIhNxVy9ymX0nUm-8vKM0g5wMrP8f1ra90GFo4MgMUzvDGZhSPndTvOT3dzz5vw4-koxJax19aUUsGp4QLPBRzqBnxzvRod_EvjOZlHJW8GDqF8p83skzpjUId6iaTU1kGTy7njm6aDqACIuxKLnWfwVs95N-OW59qTEXo5H7vpVvbotQ8vNp7YstIm7IVBrApv3wLUUOn6hWiICDJADo8VBfrXLlxfnE1YXxZ5HDOcc9fQUafmxzPIJ1YTnha2dxjSVLfmu-DUCXH8tzCl9EmYsbLqNnYDzk6CIBr83ZC4J7pxFo89SCRQ6FyTDi5e3_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=rq2v_dHUJTdorFwqyMBBIhNxVy9ymX0nUm-8vKM0g5wMrP8f1ra90GFo4MgMUzvDGZhSPndTvOT3dzz5vw4-koxJax19aUUsGp4QLPBRzqBnxzvRod_EvjOZlHJW8GDqF8p83skzpjUId6iaTU1kGTy7njm6aDqACIuxKLnWfwVs95N-OW59qTEXo5H7vpVvbotQ8vNp7YstIm7IVBrApv3wLUUOn6hWiICDJADo8VBfrXLlxfnE1YXxZ5HDOcc9fQUafmxzPIJ1YTnha2dxjSVLfmu-DUCXH8tzCl9EmYsbLqNnYDzk6CIBr83ZC4J7pxFo89SCRQ6FyTDi5e3_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی: علت این‌که ۲ میلیارد دلار ارز برای بازار تامین کردیم این بود که به ترامپ و وزیر خزانه‌داری‌اش بفهمانیم مشکل تامین ارز نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72905" target="_blank">📅 18:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72904">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=MA7w6yjsXB029H026DUCxqDrm3husItGur9KvTDl6hzVT6cGsTrt7ruIMqqBAos1GiftbbOATD2g9oD_WhQd4Bjk63AESZkx3jnIsvPxLiuyqTO92NTbATaqhzhYMlKFOBwBn-wTRBbHJnuMMxaRhHZ_CH_78AALa_hyMT6Fd0Ys3Nw83Ms0Auy4gm1yZMzuetdKBMujMR3YFwIA_z6SuuoZWVkpW-yNDvnqJOW6ihWVAedDzFQ8EDvcGH3XZmKwfClj-LZQIVWCWukDOtGwFyLpgtXLb3YLLD_huEsCNWX7WItrV6mGZc67rOZorwald77dY0nyoSOZLDU6_keLOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=MA7w6yjsXB029H026DUCxqDrm3husItGur9KvTDl6hzVT6cGsTrt7ruIMqqBAos1GiftbbOATD2g9oD_WhQd4Bjk63AESZkx3jnIsvPxLiuyqTO92NTbATaqhzhYMlKFOBwBn-wTRBbHJnuMMxaRhHZ_CH_78AALa_hyMT6Fd0Ys3Nw83Ms0Auy4gm1yZMzuetdKBMujMR3YFwIA_z6SuuoZWVkpW-yNDvnqJOW6ihWVAedDzFQ8EDvcGH3XZmKwfClj-LZQIVWCWukDOtGwFyLpgtXLb3YLLD_huEsCNWX7WItrV6mGZc67rOZorwald77dY0nyoSOZLDU6_keLOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
مجری: «شما در سازمان ملل گفتید: «یک روز، که شاید این روز چندان هم دور نباشه، مردم ایران آزاد خواهند شد.» منظورتون از این حرف چی بود؟
نتانیاهو: «مردم ایران خودشون می‌دونن چه زمانی و در چه شرایطی باید کاری انجام بدن. وقتی زمان و شرایط مناسب فرا برسه، اون‌ها به پا خواهند خاست و این حکومت سقوط خواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72904" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72903" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvuxRH_uXu06uDALxc5YHaZlmQnpOyX4ZGoZuqrztFRiEVjVHX_HF39ehi1XEe2hYmtznio0X6U6r2WZmSXmI4p7mZfi5na_JFxrNXJIudR_CLUVosRKSsrofuaEyqKb6KzUd6bIhw20oNxRO8lkA7SYkktbUSpqM2YtTc0kHE6Hz5iajq6WbF6XFTff6bjkGZVfIIUr5OOg_EW3iB8fDme59rN0593X4lJ8C0aKS9iyuO_AK5TpHkexGOUfdGYPC6S5uxZnDj4FReqQE8YHc8uxOijM2XrWu6eqAuvU_vWCt-CHglm0QU4o8N6N7jTOaOEBDIkb5oCHUnHdaqWynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72902" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=oEhXOaqi6ea8jnRw59pn_QpPZ6LkvHuDpkn70cIufZERGBe--AtxeJssAidFRzNZUkHTdwJ4_e5onZ4i-sKyuMjvhgCeyUGnbTuFSqhTavftY0qc6sSfhHqTAIT8NGQTd8tEEekFanScGlyDdK43IAbKHMY-fSQDUlrV_HfyKBGMOljX3ygmfPoxPFWLDkuZde82ju4q2jwbn0zsy1fV1O64qAuUbDXHfHrJiUGK5alrUuKj13w_lKVsbQCKXGv1r_ulRD2OGKJggT4MAXwLB_aoHA-triJNVxEIXa2-CIImF1LzdoDSXbMx7WhjQpzHZXlkneq2p7h7N3kpvY7RHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=oEhXOaqi6ea8jnRw59pn_QpPZ6LkvHuDpkn70cIufZERGBe--AtxeJssAidFRzNZUkHTdwJ4_e5onZ4i-sKyuMjvhgCeyUGnbTuFSqhTavftY0qc6sSfhHqTAIT8NGQTd8tEEekFanScGlyDdK43IAbKHMY-fSQDUlrV_HfyKBGMOljX3ygmfPoxPFWLDkuZde82ju4q2jwbn0zsy1fV1O64qAuUbDXHfHrJiUGK5alrUuKj13w_lKVsbQCKXGv1r_ulRD2OGKJggT4MAXwLB_aoHA-triJNVxEIXa2-CIImF1LzdoDSXbMx7WhjQpzHZXlkneq2p7h7N3kpvY7RHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تریلر Gta نیست، ایران خودمونه!
چند روز پیش توی بازار آهن تهران، یه نفر با ماشین میزنه به یه موتوری و فراری میشه، پلیس هم میفته دنبالش.
چند تا تیر میزنن به چرخاش و در نهایت گیر میفته و حسابی کتک میزننش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72901" target="_blank">📅 17:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=RdK98ZA3krxZaTb1A_ir-1-ZmXK6e65JCwYnY3JiUG1yELu0VwFqVdbwEQxO-W0ap2_ITO47o6lP2i9oGAAi6RVn41iz2o-KyfqPIPzRi4yoFDL7JJhftuN9U3QiO4m4gHKogyH25sy3pSMd62aMjpmBoFnBfCJDSHT6vbLdK3KWfWS37SozN8aPlL60DAFTjCjEdASiMU8EMi9KZhQG-JRYW-jP13r8YMS1WZHtkPy6IiwM6WYfPwqKYLQ9kncLYFYumQvaoUgARYVFjDRYZOjlardNjqs13LsdFms3Awn5_Cg2yFsL4aNSuDFBf1UAArbQv0Min6tCc3KsuHKOIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=RdK98ZA3krxZaTb1A_ir-1-ZmXK6e65JCwYnY3JiUG1yELu0VwFqVdbwEQxO-W0ap2_ITO47o6lP2i9oGAAi6RVn41iz2o-KyfqPIPzRi4yoFDL7JJhftuN9U3QiO4m4gHKogyH25sy3pSMd62aMjpmBoFnBfCJDSHT6vbLdK3KWfWS37SozN8aPlL60DAFTjCjEdASiMU8EMi9KZhQG-JRYW-jP13r8YMS1WZHtkPy6IiwM6WYfPwqKYLQ9kncLYFYumQvaoUgARYVFjDRYZOjlardNjqs13LsdFms3Awn5_Cg2yFsL4aNSuDFBf1UAArbQv0Min6tCc3KsuHKOIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم در جستجوی کار:
بعد دیدن یه آگهی منشی مطب با حقوق ۱۵ میلیون تومن رفتم مطب اقای دکتر
خیلی همه چی هم شیک و با کلاس بود؛
وقتی گفتم برای کار اومدم اقای دکتر(آلت متحرک) بهم گفت اون ۱۵ میلیون حقوقی که نوشتیم فقط ۶ تومنش برای کار تو مطبه و اگه ۹ تومن بقیشو میخوای باید به خودم خدمات جنسی بدی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72900" target="_blank">📅 17:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72899">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=LHP4LDJdZcTyZGcRajOMlTZGCCf2RrZ30vSdigQK1J4evx7Ga_AkC6Ok3HCK1AJnyiO98MPrFqA-KnDQEazu3dgtfIDGl19OhOGti5uLOsDK6CJl0xIVWBCXAEM7LdXvMOLkv-K6xano7ILplVvg76I5fJPaGsymOtrlm3NJRfH9HF7BBzdVNk75C7O3DLH5-yCpwyWGYN9ycWSSJAKVbc7gXDFU_dgERSvNyhx_b1-uaplKLdsiGSIQulxCKngeH6zgcz_Zjl0jqu07E3bfYswBAeJUHKc9lkgx8TYF2J66fwgcT-EfrdIEY7NVAA54S9-fF1Do5_sL5ozCYdM5mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=LHP4LDJdZcTyZGcRajOMlTZGCCf2RrZ30vSdigQK1J4evx7Ga_AkC6Ok3HCK1AJnyiO98MPrFqA-KnDQEazu3dgtfIDGl19OhOGti5uLOsDK6CJl0xIVWBCXAEM7LdXvMOLkv-K6xano7ILplVvg76I5fJPaGsymOtrlm3NJRfH9HF7BBzdVNk75C7O3DLH5-yCpwyWGYN9ycWSSJAKVbc7gXDFU_dgERSvNyhx_b1-uaplKLdsiGSIQulxCKngeH6zgcz_Zjl0jqu07E3bfYswBAeJUHKc9lkgx8TYF2J66fwgcT-EfrdIEY7NVAA54S9-fF1Do5_sL5ozCYdM5mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی از اینستاگرام پکیج پولدار شدن خریدی و خیال میکنی دیگه کار تمومه...:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72899" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72898">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=G4BeShXXD7lNFA4pciDkQd6dvmLMW0MetKFcMEJLOqxZGjOqgUQR5FIwJ52Mbqkq3MarcbpWRLtyTjxTUbU1dvFVtvD8DOrt8e8RZ59ej_ryFqUr_v4GTurfDfW9oSMclH1kM2z7DxJGEHDVejdD8k2Widigcteqdp4NB2PSjluu1autS2cy2qihxdUenl52SBfGAcNjK3Q4fuGQucSvwDyYDLDGVQsQt2V0de1SxBz7lOdqKRbEljoh_ujLt-W5R4_QUm5pwUaW6mg1rDYfh_GT7OIhOiABAsKlqB8n3UUHgvcQaRy6FkStIrQQMh_uLo0lYy9f4nvghgmzl8F_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=G4BeShXXD7lNFA4pciDkQd6dvmLMW0MetKFcMEJLOqxZGjOqgUQR5FIwJ52Mbqkq3MarcbpWRLtyTjxTUbU1dvFVtvD8DOrt8e8RZ59ej_ryFqUr_v4GTurfDfW9oSMclH1kM2z7DxJGEHDVejdD8k2Widigcteqdp4NB2PSjluu1autS2cy2qihxdUenl52SBfGAcNjK3Q4fuGQucSvwDyYDLDGVQsQt2V0de1SxBz7lOdqKRbEljoh_ujLt-W5R4_QUm5pwUaW6mg1rDYfh_GT7OIhOiABAsKlqB8n3UUHgvcQaRy6FkStIrQQMh_uLo0lYy9f4nvghgmzl8F_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از سورپرایز تولد علیرضا توسط مامانش. دخترا اگه نصف عشوه علیرضا رو داشتن سر خونه بخت بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72898" target="_blank">📅 16:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72893">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnPPoksUHkYbhob8x6itiLYB6SLuhTc9vcIwdNL0kKQTYjMe5Q_ndJWd4VUzrL9RCkISKKTPonT5ofbHu1T6tS9SYC-1ZmBFe9hzIVfFmWmZyrpZF_-PCJzaZQK84sxvDV8urbPKsM4R8n8H7RGn88cO9Rs7aCk9EluGfQCil3kqhDlhzedwjSjL95mX0fCzr7FYgi-TIVNveXACBJD5khbLB0SjbRGUSzNADCD9a-RXGi7jSXnzfNUCtbERQNDjYS4XAMWPij-SSGyP8thUcYNrFeJAY3Z0BVSLUTpm34YIXyh2vulh0m_kd8Dikc1AlvQr4GI4RBxk3guIQVtGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpDeFgfJqTg2Byuu506W672uDK--JA3blQMWnnYpDliGNKkb-dTVk6dkQTQkCT5hHJjASfDqrcjf2x43cF4R8NgbD75VKdxc6dIwJAW-BKmf0m0KSuX1VjJZPPWMbXOgFLSniLKcEkDBH-kdno7mnlq7E6EgC4Pr8zflWbpd0aCS-g0eE8gt2C0FlcJofnvmBVe4PasIi32Ajong7P1oxdxZT9awDOdRS83EBF6kHPuJ0BR7V1HleAddW2vS9rqA0vdDWousGmHFfRpGrE6z0HkCYwABAW2VI9BgRpdWgZYhw6pwHHnd2LCjKnNnNqCR0vqDFrpuU__HhNMIYQ0MtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=RJv80UqWJAgMuwuZnQOwU1Hqk_LgOdiohmbdIecE1fkjamfO3yy4MNoYG0XV2UfX1rJFdknYq8gsjBHD_clmPI0go8mDoRRioGLFaaP7qKbw6jbnDqbl-H-QcS07jft4ykvAyjHcf5rnMaGw294cwH9k8qxx2k4c-H7QIZ8FJ34bh9-Wt4AFwnuwd1-zB649sKCUDAL2gA9nn8PLX0ObR88KnEBt90AjHdIBB7A6VWCz4xkS1Q3xSoM3rXs97eNLoAAajF6Qg2G-p5uv5gcu4fpZcl5D3mFONVg00sAk_AAgYdgDTU4HitRKuuPZ3EU7TF9qavsBOzshD5ST7l0ktw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=RJv80UqWJAgMuwuZnQOwU1Hqk_LgOdiohmbdIecE1fkjamfO3yy4MNoYG0XV2UfX1rJFdknYq8gsjBHD_clmPI0go8mDoRRioGLFaaP7qKbw6jbnDqbl-H-QcS07jft4ykvAyjHcf5rnMaGw294cwH9k8qxx2k4c-H7QIZ8FJ34bh9-Wt4AFwnuwd1-zB649sKCUDAL2gA9nn8PLX0ObR88KnEBt90AjHdIBB7A6VWCz4xkS1Q3xSoM3rXs97eNLoAAajF6Qg2G-p5uv5gcu4fpZcl5D3mFONVg00sAk_AAgYdgDTU4HitRKuuPZ3EU7TF9qavsBOzshD5ST7l0ktw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۷ اکتبر، سومین سالگرد «طوفان‌الاقصی»؛ حمله‌ای غافلگیرکننده که سال ۲۰۲۳ توسط حماس و گروه‌های مسلح فلسطینی انجام شد و حدود ۱۲۰۰ نفر در اسرائیل کشته و ۲۵۱ نفر هم به گروگان گرفته شدند.
بعدش اما ورق برگشت؛ جنگی شروع شد که نتیجه‌اش ویرانی بخش بزرگی از غزه و کشته‌شدن ده‌ها هزار فلسطینی بود. اسرائیل هم از همون اول گفت قرار نیست ماجرا رو همین‌جا تموم کنه و دنبال کسانی می‌ره که در حمله ۷ اکتبر نقش داشتن.
و این وسط، فهرست ترورهای اسرائیل هم کم‌کم بلندتر شد؛ از فرماندهان حماس و حزب‌الله گرفته تا چهره‌های ارشد نظامی و امنیتی جمهوری اسلامی؛ یعنی جنگی که قرار بود با «یک حمله» شروع و تمام شود، سه سال بعد هنوز کلی حساب باز و بسته‌نشده پشت سر خودش گذاشته.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72893" target="_blank">📅 15:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72892">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PocDC3eX55oCnESSBdobD2aygQEaKGrzQ8_W6WwC1Vs6-5wPrn5pgkfle-ZmZgpFZC0fbx00WE4rwkTN18vKqDwBDUpPepO3r3KT2HBVMeBXQ3cTNBaNuhSGynAFHj6tOQNKvGfGpsLkdZuy8J18cVCsrTHDKV9yc9x_vFanAMrIztgM3mtqF8AA0dcTQ7L4MessVbzIXOVCUFf1WmEm5UxN2iGE7f_6hmjqETAdoA_3XYvVnOoEJEH7uezrbXCWSYuyQwvbZjy9m7jVjjCOpudXqpBjHdSzJOsswax4SVkZLFf3eqkDZLJ4GNIy49GvAiiwZ2GKmDSLidFvPdUbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه‌های برتری که مدرسه فرهنگ (وابسته به حدادعادل) تو کنکور امسال داده :
زرین، پسرِ بادیگاردِ علی خامنه‌ای : 16 انسانی
محمدباقر، پسرِ مجتبی خامنه‌ای : 106 انسانی
محمد‌امین، پسرِ بذرپاش (وزیر راه سابق) : 173 انسانی
محمد، نوه حداد عادل : 910 انسانی
محمد، نوه محسن رضایی : 1700 انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72892" target="_blank">📅 14:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72891">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=lUniwBUgHzQt0L5DUctDrqGG6SFAAqBKTEFwWBEcRmljERgR8IvU07tK8YO6K4T_JZ4YIZnfJXImY-DjRdKIcOUAphdLVogzxDPc_8UJdyYS9znJavERrejtywdwkKhpqHGOvcIhg4tDy_h4Kgorqq0NZEzn_3cLX4uzkk7FEgySOzY8r5dL9q7Yua7O5nkAW8jSXoxNSlj1q57fEArgcytcboShnigtWojXZDWVmYbdYnZUTJnH_lYnn7igDNiT6VsLAyHZgYKNcKXE2d3kv26nXPS7pmcmEyvCrCYcDCeD-HJnMRZBNygN4ZMawD4Tn263dZV7pELskEotS6Bqgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=lUniwBUgHzQt0L5DUctDrqGG6SFAAqBKTEFwWBEcRmljERgR8IvU07tK8YO6K4T_JZ4YIZnfJXImY-DjRdKIcOUAphdLVogzxDPc_8UJdyYS9znJavERrejtywdwkKhpqHGOvcIhg4tDy_h4Kgorqq0NZEzn_3cLX4uzkk7FEgySOzY8r5dL9q7Yua7O5nkAW8jSXoxNSlj1q57fEArgcytcboShnigtWojXZDWVmYbdYnZUTJnH_lYnn7igDNiT6VsLAyHZgYKNcKXE2d3kv26nXPS7pmcmEyvCrCYcDCeD-HJnMRZBNygN4ZMawD4Tn263dZV7pELskEotS6Bqgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوچک زاده نماینده مجلس:
به یوسف پزشکیان بگید یه بچه دبستانی از پدر تو بیشتر میفهمه!
حرفایی که تو میزنی باید امریکا بزنه نه پسر رئیس جمهور ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72891" target="_blank">📅 14:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72890">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=Rk4jJQ8Y2unpMMda7ya77sxZbo8ZoY0msSwXZxXxuHoDGmwXA9noeH2Sp5-EzA4b4YYYon5atYDeyMxDePg3LiiitK3g70Ij_GVy1VOK3lV2Q_Wjr4nhLXB-wCrpF8VEpvZ375PhfopdeKdP-1eI5MYO4fxnn-kCRXH2v-WhW46pLrYG2mgzAjzzHPGTIUSJ9bBbHVKLadzeltb0BmpVqxqbqDsGNSZDwiWzJP3MNrzYFs5HzWFH8yKtM5JQ-Wtd5EG5z3ThOjq0gO9M6qtDkUy70KFx4S7lJPt-8I5vKmnz8TKHUr6YbhBklqU_EbY8kZSK61_arXrmk7vyffyObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=Rk4jJQ8Y2unpMMda7ya77sxZbo8ZoY0msSwXZxXxuHoDGmwXA9noeH2Sp5-EzA4b4YYYon5atYDeyMxDePg3LiiitK3g70Ij_GVy1VOK3lV2Q_Wjr4nhLXB-wCrpF8VEpvZ375PhfopdeKdP-1eI5MYO4fxnn-kCRXH2v-WhW46pLrYG2mgzAjzzHPGTIUSJ9bBbHVKLadzeltb0BmpVqxqbqDsGNSZDwiWzJP3MNrzYFs5HzWFH8yKtM5JQ-Wtd5EG5z3ThOjq0gO9M6qtDkUy70KFx4S7lJPt-8I5vKmnz8TKHUr6YbhBklqU_EbY8kZSK61_arXrmk7vyffyObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو درباره ایران:
«کشورهایی که حتی به ما حمله می‌کنن، یواشکی و در خفا می‌گن: اینا باید سقوط کنن؛ دارن همه‌مون رو خفه می‌کنن.
ما مطمئن می‌شیم که سقوط کنن. سقوط می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72890" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72889">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=KJkvT_-pI74kpYZU0dHhoHgzD-TjR_T3zcpmSmCDikN8I7Iw5xa1b_lPjcc80lncBwpL5vy2cuO-Ck0B-FyDLusI8cYZ2fg5qbKLjMtJvB4Bvw8lHmvuVojkTTCOXJwD7w_5cm5VXxsaAfYkyhe5lDQ-2HhwA8LWF_S9rGQrtTHYltZjhwNgwmvKt28ByRvToqBtjeUYD5A4k4dztomTiXgSj6pXuAt0wkYjJxxHejMXM3DLjU8h4UmRBn59-_v7kHg8jIV9-SixnYDIGcCOf3zpwFmWADyXIogaA4GFE8tWEZ9CjN6wp4k4MGvhjfwv3XRk1OXrU9c4P8YZGq-alQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=KJkvT_-pI74kpYZU0dHhoHgzD-TjR_T3zcpmSmCDikN8I7Iw5xa1b_lPjcc80lncBwpL5vy2cuO-Ck0B-FyDLusI8cYZ2fg5qbKLjMtJvB4Bvw8lHmvuVojkTTCOXJwD7w_5cm5VXxsaAfYkyhe5lDQ-2HhwA8LWF_S9rGQrtTHYltZjhwNgwmvKt28ByRvToqBtjeUYD5A4k4dztomTiXgSj6pXuAt0wkYjJxxHejMXM3DLjU8h4UmRBn59-_v7kHg8jIV9-SixnYDIGcCOf3zpwFmWADyXIogaA4GFE8tWEZ9CjN6wp4k4MGvhjfwv3XRk1OXrU9c4P8YZGq-alQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هر دلار و هر سنتی که این حکومت به دست میاره، خرج جاده و پل یا بهتر کردن زندگی مردم ایران نمی‌کنه.
این پول رو خرج حزب‌الله و حماس و شبه‌نظامی‌هایی می‌کنن که از داخل عراق موشک شلیک می‌کنن، و همین‌طور حوثی‌ها.
باید پولشون رو برای مردم خودشون خرج می‌کردن، اما به‌جاش پول رو صرف تروریسم و تسلیحات می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72889" target="_blank">📅 13:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72888">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=vSXbb3b3t5cfp_bkG-ZWyfdXmufyEd7kwRNfRAHA8KG1choIy0WedpdjdLYN7Hitn97-mtuvq6koE5EqAluerTI8zKBLepQIub4UWq2oqRvt6I44tgcSGwMUVtu5dYAcmdBQOnHs6HHDngiMp-SjR-KhYtGj9JiZlMCH6Th4DscUXVa3xRARyu763Msk_lzL4OzE8oerjk2HKqPUyQGOPYxe-5sLmj-fAwXY5ijXxHzaziQQkfW6mttObhLgLTZ_uC3_dOZMyu1KI46ksBT_ymHgVZNxuj0kLvaRzaa6xYs0mSqXcuRgh-QyBZbbHSZpol9pNzTFkrXOJ5EOUrbNjpb8mIairXYEUqgDHhCl7iDiq7KL--5wqoV0gYgFtT_8SGMz7c8BOn346qIiUYIvX5ffrfZjmQR8Ot4FUZcsSvZzu8ivEr16rh8EQD3We7we99FaNk49AxkuvealUGx30jBFaYEWQnYfzo8naj--SNCBmiOESAAKD0tXZwHRI4P0YIrZZY_kHkJ00TQqrmLAGWurBbfCT6EGRsXpJ92DPauGIQ6qZW21GcPPpSAXpKy3lhHx4H5sxNRDeLn-DriWsG-3xHi6Szz2HYJP9Y38OFGfqAOpkR8-bPXxn8hB8JgpRZrYZxC3Pk7HvqL85gP0NJrOfXD2-UwsqnEpyKb7vQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=vSXbb3b3t5cfp_bkG-ZWyfdXmufyEd7kwRNfRAHA8KG1choIy0WedpdjdLYN7Hitn97-mtuvq6koE5EqAluerTI8zKBLepQIub4UWq2oqRvt6I44tgcSGwMUVtu5dYAcmdBQOnHs6HHDngiMp-SjR-KhYtGj9JiZlMCH6Th4DscUXVa3xRARyu763Msk_lzL4OzE8oerjk2HKqPUyQGOPYxe-5sLmj-fAwXY5ijXxHzaziQQkfW6mttObhLgLTZ_uC3_dOZMyu1KI46ksBT_ymHgVZNxuj0kLvaRzaa6xYs0mSqXcuRgh-QyBZbbHSZpol9pNzTFkrXOJ5EOUrbNjpb8mIairXYEUqgDHhCl7iDiq7KL--5wqoV0gYgFtT_8SGMz7c8BOn346qIiUYIvX5ffrfZjmQR8Ot4FUZcsSvZzu8ivEr16rh8EQD3We7we99FaNk49AxkuvealUGx30jBFaYEWQnYfzo8naj--SNCBmiOESAAKD0tXZwHRI4P0YIrZZY_kHkJ00TQqrmLAGWurBbfCT6EGRsXpJ92DPauGIQ6qZW21GcPPpSAXpKy3lhHx4H5sxNRDeLn-DriWsG-3xHi6Szz2HYJP9Y38OFGfqAOpkR8-bPXxn8hB8JgpRZrYZxC3Pk7HvqL85gP0NJrOfXD2-UwsqnEpyKb7vQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
«اقتصاد ایران داره به نقطه‌ای می‌رسه که از نظر شدت وخامت، فقط تعداد کمی از کشورهای دنیا چنین وضعیتی رو تجربه کردن.
و تمام این وضعیت تقصیر روحانیون شیعه افراطی‌ایه که توی اون کشور تصمیم‌گیری می‌کنن.
همین‌ها هستن که مردم بیچاره ایران رو به این شرایطی که الان توش قرار دارن، رسوندن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72888" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72887">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAH4ZWaDCtalzUQQvXcR3Owa0qI23wvPJxl6wazGsv7QN2Oo1EOU9ZpHofUwUxT4xcR7dVrh7_PxAum_CTlI0obnpQXJHLZQSpn7mOvMx8WM5vceyXJOhzm-AZXTM7MklyIN8FRw6fM-_snMsuDqrwDUepSGxBQDLq0xAd_wwhrMBiV7a0MskPAfXrokc7OUhV-kRQxMB78XJUwwiX9pRRR5WBoJtpIAe0mzYEeCkau54A9Ql-etW7Cj2M-Krod8YPNaQKJn-ibOsTgm1TtVnDeItYz-tZMmr4eT6LUL0irnQBxuvb75PetnCo6PExrA7SsH5V06cfx5vP5bPgrzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، به رویترز گفته آمریکا هنوز دقیقاً نمی‌دونه بعد از کشته‌شدن علی خامنه‌ای، چه کسی در نهایت تصمیم‌های اصلی ایران رو می‌گیره.
ونس گفته آمریکا در حال مذاکره با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه است، اما مشخص نیست این دو نفر در ساختار فعلی قدرت ایران چقدر اختیار و قدرت تصمیم‌گیری دارند.
او گفته یکی از چیزهایی که آمریکا متوجه شده اینه که «کاملاً مشخص نیست ایران چطور تصمیم‌گیری می‌کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72887" target="_blank">📅 12:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72886">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFZbpKrOd_OokJyV9POLL0T4fKvYUEJRTcYTbREW9LvSFUMebZ221_wTlBSwTruxdEmsDm9jj4u3zWBYXf6WbEjfZH-oiNerSbKmjL6EGD6W1drDDdDwTiRokMZZWWZ91XeI08L4Y4TVKH_GqrGKaUo2nebL62z6DMsv4YE1Igl0e55OwsDxzuQY27O0J7hKkvjdgVtqJYMQ6W1ICrxxumBAlSVFcNecbZuayjv8ZcyI0obMXbeKxydgF748JtGq6XvEUJBXDfT5ZfVolJyDOhYcjo6Ff2SG2WQFZyQoJmTv4j_h9kTcKflqwe6L7Rzfp1d--s1-SGHzvbAnYUeb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، معاون ترامپ، به رویترز گفته اگه ایران بخواد به توافق برسه و جنگ ۷ ماهه با آمریکا تموم بشه، باید ظرفیت غنی‌سازی اورانیومش رو به‌طور قابل‌توجهی کاهش بده.
ونس گفته آمریکا دیگه به وعده و قول برای محدودیت‌های آینده اکتفا نمی‌کنه و باید اقدام واقعی و قابل لمس از طرف ایران ببینه.
اون همچنین پرسیده: اگه ایران واقعاً دنبال ساخت سلاح هسته‌ای نیست، پس چرا باید اورانیوم ۶۰ درصد غنی‌شده داشته باشه؟
با این حال، ونس گفته آمریکا همچنان برای توافق آمادگی داره، اما امتیاز هسته‌ای واقعی از ایران می‌خواد و تأکید کرده: «قرار نیست حرف رو با عمل عوض کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72886" target="_blank">📅 11:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72885">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=BDz6SVIr5H034oicRIl1xqqVeKMLHanA-6tiEvmYBParNRP1FdH6y2zeIS6ZcrhfBfC2Pk0nWhlEPJ1z1bzRsoq5seUWKjb3vLgXy4Z8NvNN1VuaTRCCn_0YzxDJuhjBRY4Fvzxls-1npj9TL8PpS4zE3idfXxCQ1KDY6EfoU9oXUYnNp6H6lBjwsFGUfAZFuLiD7hug7yIKoWEKBJbuSV8qNrOcWYORSoq_w_odhYHdQazDQx8iu9QHC2-_Bbc5JXvPCAEOv2nRwKWpRyd02dxFr27ClHmgHKVyjwPthSbQ2bPN-LjBnXAMDvmR7hSNEfbPxZsWkki1AuinbsBRmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=BDz6SVIr5H034oicRIl1xqqVeKMLHanA-6tiEvmYBParNRP1FdH6y2zeIS6ZcrhfBfC2Pk0nWhlEPJ1z1bzRsoq5seUWKjb3vLgXy4Z8NvNN1VuaTRCCn_0YzxDJuhjBRY4Fvzxls-1npj9TL8PpS4zE3idfXxCQ1KDY6EfoU9oXUYnNp6H6lBjwsFGUfAZFuLiD7hug7yIKoWEKBJbuSV8qNrOcWYORSoq_w_odhYHdQazDQx8iu9QHC2-_Bbc5JXvPCAEOv2nRwKWpRyd02dxFr27ClHmgHKVyjwPthSbQ2bPN-LjBnXAMDvmR7hSNEfbPxZsWkki1AuinbsBRmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند نبویان: نماز و روزه و گناه و... مهم نیست همه کار باید کرد تا نظام حفظ بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72885" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72884">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94194705f4.mp4?token=GytWhSoY6RURcS1KMlT71wSl68Ed5fhTpR5ZhAOPRRaY-PJULZONmCgabXNTrAOQzyjMrnvJGa8tHHwELN0qx0fnEY2Kik16wOptDI7h-6ZRmM7ddThJIhZstaYMwDRonH8VSqx4usnnrybKLL0sBjLuE8ndmroQPWUMXpQPBEy7Slw8HN8xwUbyUR2yiK-ZbSzcGoiXc_cFtYjSJeqVkE5DUyvkPho3FcVn3jxgmrmstZemK-5V22no8U6KJFEuqltXkao1hmso-iUs_S5s6EdA9iWAnBxlyokzn9jQmCcGWH8m_kezoLUZvR3z6r5w0ZvW5EUDG6JwLFI6pFuvJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94194705f4.mp4?token=GytWhSoY6RURcS1KMlT71wSl68Ed5fhTpR5ZhAOPRRaY-PJULZONmCgabXNTrAOQzyjMrnvJGa8tHHwELN0qx0fnEY2Kik16wOptDI7h-6ZRmM7ddThJIhZstaYMwDRonH8VSqx4usnnrybKLL0sBjLuE8ndmroQPWUMXpQPBEy7Slw8HN8xwUbyUR2yiK-ZbSzcGoiXc_cFtYjSJeqVkE5DUyvkPho3FcVn3jxgmrmstZemK-5V22no8U6KJFEuqltXkao1hmso-iUs_S5s6EdA9iWAnBxlyokzn9jQmCcGWH8m_kezoLUZvR3z6r5w0ZvW5EUDG6JwLFI6pFuvJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم زیبای و ویژه برای وداع با مسی با نمایش پهبادی در آسمان!
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72884" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72883">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72883" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72882">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm3uFFygHKjvhx2Q__f_AxWNvZokZ91pxpHg0wOwQUaE-fQBMIi6YQfcUlZKW5AO5bC5Vf0Jk3fs1QXElYTLZCwhn8W8eV6NmyyFQ7jywSbU7Yczw1_aZlLNt29XgMIEB5T0eWVdtYu4Lw8PZEXPNXBHYiieEuAX1cQjsIqcefxffFmlKsvrMJBfm7FR7GR51u87iKTxXvtrhHIpA0rE9uAun0uywoy2pvLu_aanV663nVNteQ84wW4ZJrD5zxfZAAxghQ9fVz2bOkKorcuy7n0iwQaJtVbqk0rCfp_EI8RHSA4hNIr0Fx8t0Js-MDfjge2IBBZ0ZYP1sY6uFTZpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72882" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72878">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=N2YVPTE6BHsKqjpT93nEvve6YzygvL_RUnihWGjxYjEoH86OIVTUCsZLl5IwqzuqCjRNjWw1oL0rZk1VXw5E_8HII0hU3dz3j76XLuyc_8Kjyuo7RzDPnKq1n6BuncnDvxoc6dBffFhBiw9dQ3CLyGlRdCw0r4trAEzoDJBNDffISbT8QqEaaaEvBVHq7-jOZijTXYiSp-fFmQzktuz5Vio0w0rvKYkD-UTKtlgcteuPwI3K0hQLLMYMObwpS_f_0UaJASeq1ruhNmBBpOD16yShsYISPv-9OAudGTg_KjGRndcusXMrAZ_Xa48mTImQy_iCXW0WH83HU_VzP_QxdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=N2YVPTE6BHsKqjpT93nEvve6YzygvL_RUnihWGjxYjEoH86OIVTUCsZLl5IwqzuqCjRNjWw1oL0rZk1VXw5E_8HII0hU3dz3j76XLuyc_8Kjyuo7RzDPnKq1n6BuncnDvxoc6dBffFhBiw9dQ3CLyGlRdCw0r4trAEzoDJBNDffISbT8QqEaaaEvBVHq7-jOZijTXYiSp-fFmQzktuz5Vio0w0rvKYkD-UTKtlgcteuPwI3K0hQLLMYMObwpS_f_0UaJASeq1ruhNmBBpOD16yShsYISPv-9OAudGTg_KjGRndcusXMrAZ_Xa48mTImQy_iCXW0WH83HU_VzP_QxdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسیدیم به اون لحظه‌ای که عاشقان فوتبال تحمل دیدنشو ندارن...
لیونل مسی، اسطوره ۳۹ ساله فوتبال، سه‌شنبه ۶ اکتبر ۲۰۲۶ برای آخرین بار پیراهن آرژانتین رو پوشید؛ این بار در ورزشگاه مومنتال بوئنوس‌آیرس و مقابل بنین.
مسی بعد از سال‌ها افتخار، جام‌ها، اشک‌ها و لحظه‌هایی که برای آرژانتین ساخت، جلوی چشم هوادارانی که برای خداحافظی باهاش ورزشگاه رو پر کرده بودن، رسماً از تیم ملی خداحافظی کرد.
از این به بعد دیگه مسی رو با پیراهن آرژانتین نمی‌بینیم؛ پرونده یکی از باشکوه‌ترین دوران‌های ملی تاریخ فوتبال هم اینجا بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72878" target="_blank">📅 10:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72875">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=YNW3XmuatFQNxK_gj0HwyQ3dgq1_sOPNP0FKIxQYUhf63nvbEZK1j7-3zJm6_mt3tCqvfaT5yBxh8XDT_YgaOk8IOs5N1QIRGlT-XB4A6ddQQJIHkIhcka7hv00DmQ--JT7_SNOTVK3R9qeJcOkOQXmjGJNYBUMA55JL9SRmu-PFFb9g-3_8mxdOjcf6TWkX9Su-A9L6cLSeLdjrMR6aPr0qri1vX7iaYK4mxRc7LpOBSXnm-H1OPvL_ZiXRkx9bs1T_qmium1d_P9jJPJ5QGeGg9RBLu6iuqqFqsVqQf7ikG8IXThfQh8A5Y0bpFbQQE8I5A1Y-Wkjf2AqSONwFXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=YNW3XmuatFQNxK_gj0HwyQ3dgq1_sOPNP0FKIxQYUhf63nvbEZK1j7-3zJm6_mt3tCqvfaT5yBxh8XDT_YgaOk8IOs5N1QIRGlT-XB4A6ddQQJIHkIhcka7hv00DmQ--JT7_SNOTVK3R9qeJcOkOQXmjGJNYBUMA55JL9SRmu-PFFb9g-3_8mxdOjcf6TWkX9Su-A9L6cLSeLdjrMR6aPr0qri1vX7iaYK4mxRc7LpOBSXnm-H1OPvL_ZiXRkx9bs1T_qmium1d_P9jJPJ5QGeGg9RBLu6iuqqFqsVqQf7ikG8IXThfQh8A5Y0bpFbQQE8I5A1Y-Wkjf2AqSONwFXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ایتا و روبیکا تصاویری از یه سلاح ایرانی تو مرز ایران و عراق منتشر کردن که حتی خودشونم نمیدونن دقیقاً چیه :
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72875" target="_blank">📅 10:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72874">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=KnV5KXvmalI1tnu-sfB5D7KnK1VdydFgcAjxOYMOf1FJSf8hhpJwKhvWlhouVckehb10IIz2wO-phNETYmgZgUqxZEykx-1r9dStayaJ_mdffLfe4hFcxCOKrcPgl5JFHnOVdyn0iCt63PTsgNtiVY17an0Vm8jHt4hpnvqMiBNv2I8e1_QL_ydWCnTNJ92V5eWwJU0bkpNaY3PBul68scmo-FQd4JIxbu4Agy0uY0VZgP7YNNbil7S1V9aZ0kyT4Vrm36r_uH0kjsYnFZ7uwfE3TWAbH9_-fE8BEScZr8d9o02Zxx-prTd8Rz1R3AAs6Y0UOVaiKBRa2CKvO9WlYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=KnV5KXvmalI1tnu-sfB5D7KnK1VdydFgcAjxOYMOf1FJSf8hhpJwKhvWlhouVckehb10IIz2wO-phNETYmgZgUqxZEykx-1r9dStayaJ_mdffLfe4hFcxCOKrcPgl5JFHnOVdyn0iCt63PTsgNtiVY17an0Vm8jHt4hpnvqMiBNv2I8e1_QL_ydWCnTNJ92V5eWwJU0bkpNaY3PBul68scmo-FQd4JIxbu4Agy0uY0VZgP7YNNbil7S1V9aZ0kyT4Vrm36r_uH0kjsYnFZ7uwfE3TWAbH9_-fE8BEScZr8d9o02Zxx-prTd8Rz1R3AAs6Y0UOVaiKBRa2CKvO9WlYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72874" target="_blank">📅 10:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72873">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=tnQL83kiM9_OZdu_p1MGFCqFPtLhdD3ryaPI3gELiaieXbd-yDK8qewYs8UeQOieEYylHykiZlqlKhirYJ9avgFJkWsI1CRvY_YjqebOKnZTXt3voIsBRqnq9Yj5FY4HtJtXMrz8qAxsCslYjtMNayqbSt-hyv-c81uUzNmVrMGv5sx-x34X7KIK95MvgvGfBXbYbcJ_HAMwO4Bsc-wPBsv__qJWBbMy2AWfkvHpzh5bE80YVejJ1VjEtfWv4qiK5epgnTjxMgMOnqLbCcn7g2KQD89L_0QIy3PLSzXpBYCtdlngHk_bYShf7rgkrltzvN4EPCZ4ObIoKDdB63W6XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=tnQL83kiM9_OZdu_p1MGFCqFPtLhdD3ryaPI3gELiaieXbd-yDK8qewYs8UeQOieEYylHykiZlqlKhirYJ9avgFJkWsI1CRvY_YjqebOKnZTXt3voIsBRqnq9Yj5FY4HtJtXMrz8qAxsCslYjtMNayqbSt-hyv-c81uUzNmVrMGv5sx-x34X7KIK95MvgvGfBXbYbcJ_HAMwO4Bsc-wPBsv__qJWBbMy2AWfkvHpzh5bE80YVejJ1VjEtfWv4qiK5epgnTjxMgMOnqLbCcn7g2KQD89L_0QIy3PLSzXpBYCtdlngHk_bYShf7rgkrltzvN4EPCZ4ObIoKDdB63W6XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شک این یکی از عجیب‌ترین پرونده های فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72873" target="_blank">📅 09:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72872">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=eMeggiVwb8mgfjv_CG5S7LStXUxmgdHkq8_vZUjYfhpBY70XcsTbtp4zB5GQobMv6fr7YXZ8ZmKiezpu00BxQlN4Nb05qOsCNK4Rzq3yUoHjy3bs71BzLGRsPRMdCAxwTQWngeT24NJDHgLGYkt6aVL9G4jfVMY7iVYdhjdNuE2ofFV99QFn3ZdTJ-4_jHYB5QJm-vAXiXczIaUVrMdK4T9N0h4L3BCAhg-ZZD5S3ot6g_pDsREL2Ul52a4rrkIYjs5YCAUpYpBipHTDUwcyzcjsOSmJEvfyQ3EanIIdb91rgeJ3jPKwrx822Nlv4oVUas5rXrviy6eag7m050kv0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=eMeggiVwb8mgfjv_CG5S7LStXUxmgdHkq8_vZUjYfhpBY70XcsTbtp4zB5GQobMv6fr7YXZ8ZmKiezpu00BxQlN4Nb05qOsCNK4Rzq3yUoHjy3bs71BzLGRsPRMdCAxwTQWngeT24NJDHgLGYkt6aVL9G4jfVMY7iVYdhjdNuE2ofFV99QFn3ZdTJ-4_jHYB5QJm-vAXiXczIaUVrMdK4T9N0h4L3BCAhg-ZZD5S3ot6g_pDsREL2Ul52a4rrkIYjs5YCAUpYpBipHTDUwcyzcjsOSmJEvfyQ3EanIIdb91rgeJ3jPKwrx822Nlv4oVUas5rXrviy6eag7m050kv0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
حداقل شش ماه اول امسال، عمده کارهایی که کردیم این بود که دو تا موضوع مهم رو به نتیجه برسونیم؛
یکی کنترل تورم، چون به‌خاطر رشد نقدینگی و فشارهای ناشی از دو جنگ پشت سر هم، نقدینگی شتاب بیشتری گرفته بود.
دوم هم اینکه توی این شرایط بتونیم کالاهای اساسی، دارو، معیشت مردم و مواد اولیه کارخونه‌ها رو تأمین کنیم.
این دوتا استراتژی اصلی بانک مرکزی بوده و خوشبختانه بخشی از اقداماتمون هم به نتیجه رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72872" target="_blank">📅 09:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72871">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را #رایگان کردیم برای 100 نفر اول
👇
꧁༒VIP CHANEL  GOLD༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72871" target="_blank">📅 01:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72869">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را
#رایگان
کردیم برای 100 نفر اول
👇
꧁༒
VIP CHANEL  GOLD
༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید
لطفا رعایت کنید تا حق خودتون ضایع نشه
🙏
چون عضویت فقط برای 100 نفر بازه
هرکس سود کرد دخترم و همسرم رو دعا کنه
❤️
🙏</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72869" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72868">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72868" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72867">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EbSfAi9nXHUCpucGiBs60Cwqzt0e0RygPPmZsnblfcMNjKoCeo_0oa0zMNSY1k92paWPM05CUdwOeUgs81h0tS-zUA6YJQzdwTdBXdPJzM19Ctu2AUuj-BHFAYLrr1YXYK2mSGasNqejYUhKWEZujzRdb2sroCLdzcqCRDbuiNKccGkO9OMdEDXFTleDncgmmzv9waEZYIjP4yuqDk0WT-DjKxuKVYeZfuymoDJovKmhOpCYun7ndsJZlEVx9icI7qtFqPSyq8YRHUaUqRsPJugmsJGfbWdhGKOqH434egKL-qW6VVyqmEiKFE72jIOPW1xDfWTvRFBhnMs9r4HpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72867" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72866">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOzSzWlDIYWGlGNI1QN2Ae-nM8UoQaocdXMzagyexHLOyE4I4A3sZ0RFb4-hRodEXmGIFX6eIHlRs99X6TKA7t8ix7SZuyhVVvd75pgDS92EzyEbwO_I-rkCEuUxkQPFThbdd8khA5bgjOycYA0R-ciDAfTcURms3Uv3D2tSxkwWK_zK_b3oj_ZLKTw40_SyEUiVTd-DneXNO7-PWC8uS03Ngv3GZhhWlVqO00PljxE8JLopY_B1tPlARjGH2KzqMmp3dIgyy0HpClMkisK9sG8Muzmj_5rxbeEREGiudZhC5pInywwNLxD3_yOk4UZaQCfc4HWNFMs87nUk1rhIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا:
«ایران یه وزیر نفت جدید داره.
با توجه به اینکه ایران از ۲۵ اوت حتی یه بشکه نفت خام هم روی هیچ کشتی‌ای بارگیری نکرده، این وزیر نفت دقیقاً قراره چی رو مدیریت کنه؟»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72866" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72865">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=sbykwowvMQQ_9j-N9abbgiMalYnHEo7l_u5xiec4M-zzKsUi8D7VesCXL92NvN86-ugpPBuL_c1v6WrEOcWeovIAYbic3lfjuNAY2GE12Jk2wtBBoRniLg97POcsvIA3OcUEU84cesNchs3LrG1AYxoDdV3QHZv8xTMUYkyW8__kvV4RkbISQkYPNRX8m-a7O8SLZ-V23Y7cQNrCP6HVViGhTHp2TORcWQ7uS0Fjhg-6Pe1x6ZKWFH3tFM5JQDAARO-MtT2Ary-Tmh2tiXeGwN8oyJ-MgPOKzWoCoL7lqDlRIVOXcIGs94QYXh02OADAPYrOm0gSYIufhZhM13KApjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=sbykwowvMQQ_9j-N9abbgiMalYnHEo7l_u5xiec4M-zzKsUi8D7VesCXL92NvN86-ugpPBuL_c1v6WrEOcWeovIAYbic3lfjuNAY2GE12Jk2wtBBoRniLg97POcsvIA3OcUEU84cesNchs3LrG1AYxoDdV3QHZv8xTMUYkyW8__kvV4RkbISQkYPNRX8m-a7O8SLZ-V23Y7cQNrCP6HVViGhTHp2TORcWQ7uS0Fjhg-6Pe1x6ZKWFH3tFM5JQDAARO-MtT2Ary-Tmh2tiXeGwN8oyJ-MgPOKzWoCoL7lqDlRIVOXcIGs94QYXh02OADAPYrOm0gSYIufhZhM13KApjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره طاعون در روسیه، با پوتین صحبت کردید؟
ترامپ: «به‌زودی یه تماس باهاش دارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72865" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72864">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=NlevWb3Nk6mdXjBX_XiytRhOA3vTPyiT2p228CwBGJsVPNRbl4Z2JmikCwtSIUjHJabQgVC8iaolf82IS9kLlv4o4C38ueGlql_9OKDoWu0JnCuuGzWBdLTjB4D-oCZgwRFbrgkAH39wfEFulrRZ2wNxKpqPQEyBI0MNP4iSQH_UfFzbzjcFE_R5nuirv9mU-teYjQ8HH7c1-31qMa8q58sEMfiGYeNpkYpM9_JlXxqBtPEfTfMYXpDLbGCCHiOG9fRbwe-mzYVWHd1c_VhKx4K5iCvf6mm7NDx83a2hnsK92ZqC4SIY5gkKjRlxNr7UXwvdwJDmFqIjAZN6J_6tHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=NlevWb3Nk6mdXjBX_XiytRhOA3vTPyiT2p228CwBGJsVPNRbl4Z2JmikCwtSIUjHJabQgVC8iaolf82IS9kLlv4o4C38ueGlql_9OKDoWu0JnCuuGzWBdLTjB4D-oCZgwRFbrgkAH39wfEFulrRZ2wNxKpqPQEyBI0MNP4iSQH_UfFzbzjcFE_R5nuirv9mU-teYjQ8HH7c1-31qMa8q58sEMfiGYeNpkYpM9_JlXxqBtPEfTfMYXpDLbGCCHiOG9fRbwe-mzYVWHd1c_VhKx4K5iCvf6mm7NDx83a2hnsK92ZqC4SIY5gkKjRlxNr7UXwvdwJDmFqIjAZN6J_6tHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌گن: اوه، ما شش ماهه که درگیر ایرانیم!
ما عملاً همون لحظه‌ای که بمب‌افکن‌های B-2 حمله کردن، کار رو تموم کردیم؛ چون با اون حمله، برنامه هسته‌ای‌شون دیگه تموم شد و ۹۵ درصد دلیل این کار همین بود؛ شاید حتی ۱۰۰ درصدش.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72864" target="_blank">📅 00:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72863">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gEGbtFmgpVd8Vq940mAnvIYdrnQVjP0-ibp0AWn9wUHmxcHZhUA8TmZDw5GhZzTakxR5DrRDNHTGojh98yS19kz50Nyy9VXq5COT8-lSvPKobyahDbia5JU7vw7MwtSw6XNufGb57tELjKn4TknRM7y7MBiYtL0I1-_oBa52arbWkahGEG4UqkfileGpvtYmYytYjHiCu25ZEX1gYzs4R1_pE6KIjuqvAmUD-RZOlVMMtwoK_h7OqFU9WZnqTMQrGHNFHVSh06XZxhPGwY4ym3vP8QK_x4kiek3G7ofnET6mWhZKgUJmpj_kCPZbhYDicCR5DwyAkfcSUy6fqx6Eaq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gEGbtFmgpVd8Vq940mAnvIYdrnQVjP0-ibp0AWn9wUHmxcHZhUA8TmZDw5GhZzTakxR5DrRDNHTGojh98yS19kz50Nyy9VXq5COT8-lSvPKobyahDbia5JU7vw7MwtSw6XNufGb57tELjKn4TknRM7y7MBiYtL0I1-_oBa52arbWkahGEG4UqkfileGpvtYmYytYjHiCu25ZEX1gYzs4R1_pE6KIjuqvAmUD-RZOlVMMtwoK_h7OqFU9WZnqTMQrGHNFHVSh06XZxhPGwY4ym3vP8QK_x4kiek3G7ofnET6mWhZKgUJmpj_kCPZbhYDicCR5DwyAkfcSUy6fqx6Eaq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«نیروی دریایی آمریکا یکی از مؤثرترین و نفوذناپذیرترین محاصره‌های دریایی تاریخ رو اجرا کرده. هیچ‌کس تا حالا همچین محاصره‌ای ندیده؛ حتی یه کشتی هم نمی‌تونه وارد بشه.
اگه کشتی نفت داشته باشه، به کابینش یا سکانش می‌زنیم؛ اگه هم نفت نداشته باشه، کلاً غرقش می‌کنیم.
الان محموله‌های نفتی که از خارج ایران ارسال می‌شن، تقریباً دوباره به بالاترین سطح خودشون برگشتن.
یعنی به زبان ساده، تنگه هرمز متعلق به نیروی دریایی آمریکا و ایالات متحده‌ست؛ جای واقعی تنگه هرمز هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72863" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72862">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU6731yLopLJorSimPtxTbkrFct7dsZ2XJ8zCpTuwrEvLg91QDG1uVgtNONm4J1339WVm-OCYJetuEkd38db2cjDP98ZqwxiY_9OUx5g5u-tJtm5og3K-V7WeCmcFCoUkDr90C3s4vLpFwalxbqpIUJQ52voFnbEflfWMX9MWFSjaH88HjPRsTa8ZUJvYc_TwRI7CSAwGTGnP5yCxUUvtlnPKnMqcyT5MFa017mfvjYGdDMRywdzZSoqkoDR2JW7pKNyQakM9HgtDuLCw04v70312s-m2YWCkBwGmD3hxRZ-KZlwmztO1OuqJ5r9NuMc1GpFHLvJwhoFmD-9Z1qp2J0v7k8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU6731yLopLJorSimPtxTbkrFct7dsZ2XJ8zCpTuwrEvLg91QDG1uVgtNONm4J1339WVm-OCYJetuEkd38db2cjDP98ZqwxiY_9OUx5g5u-tJtm5og3K-V7WeCmcFCoUkDr90C3s4vLpFwalxbqpIUJQ52voFnbEflfWMX9MWFSjaH88HjPRsTa8ZUJvYc_TwRI7CSAwGTGnP5yCxUUvtlnPKnMqcyT5MFa017mfvjYGdDMRywdzZSoqkoDR2JW7pKNyQakM9HgtDuLCw04v70312s-m2YWCkBwGmD3hxRZ-KZlwmztO1OuqJ5r9NuMc1GpFHLvJwhoFmD-9Z1qp2J0v7k8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«من مدام از رهبران کشورهای مختلف دنیا تماس می‌گیرم که بابت جنگ ایران ازم تشکر می‌کنن.
منم بهشون گفتم: خب، خوبه! کی قراره پولش رو بدید؟
ما داریم بارِ کل دنیا رو روی دوشمون می‌کشیم. اتفاقاً از این کار هم خوشحالیم، چون خودمون قوی‌تر شدیم و بقیه ضعیف‌تر.
اونا دیگه ضعیف شدن؛ دیگه کارایی سابق رو ندارن. ما داریم کارهایی می‌کنیم که هیچ کشور دیگه‌ای از پسش برنمی‌اومد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72862" target="_blank">📅 00:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72861">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ درباره ایران:
«ایران یه کشور شکست‌خورده‌ست. همه دارن کنار می‌کشن و می‌رن. اقتصادشون هم عملاً به خاک سیاه نشسته.
وزیر نفت ایران هم گفته: «من دارم می‌رم، چون کشورمون دیگه تمومه.» خودش دقیقاً همینو گفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72861" target="_blank">📅 00:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72860">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=Y14npQzOtEtmDRSloABTluFYyYYWa_UMluFyWzwKnM4xbNnGwzoH3IsIZEJqse8-1DX_NeSG5lwVRtz73fjvVwfgXgANFn5TPMoy4kTANPnmU0MwJy1yADil3qpfrgD_krd1hmS_l61vJ5_FOb9n6rmIeMuwQXI84JeFi0Eb-CmFP9LohKA_D_rBQRa30VoSutrEUMkNt2yWe8ojgKqFwEIA8JLky1lnRCtOMtcdO04HY7frlyrB2-ftg2Z1MM6KG7qtVdSF05I6Air8krQPSlp4U2_4C6ZphR-jCFNige7IXAEt2vnkl-8xieLT0a_iGngN7bB4Uplb-tgXBBFxcKPxq1Bl9gHakOqiEb25X_aj7HdgvGBstghoQboa9ixPAJCbcCyRi8clOrn1r5uWJZ_yMet9Tcj8cptSdFL6u0PRR-0qIrHfCxfmb4ZgA5vYhB9oV5zm3-3DrQYbEudj_lrQWfVG1904xCUmqLEttjsP9ryONxQLGT1itGDVO6w82_mHyL7YhbW1P1za8tCQ6P_PszBTTxZr1K0aoZZz8hayzaGj-4pFQjSuscMsUkZQp9g5aqYFK5f4lJuXRgy1QK3dX6t2k_A3BV4urMzmuyBvAlW1DJ99ZLS__z4AnykqXS6CB1UfFZQXaAjVOiRBcg-aUBS4VKSdKQ1lw8KTQ6E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=Y14npQzOtEtmDRSloABTluFYyYYWa_UMluFyWzwKnM4xbNnGwzoH3IsIZEJqse8-1DX_NeSG5lwVRtz73fjvVwfgXgANFn5TPMoy4kTANPnmU0MwJy1yADil3qpfrgD_krd1hmS_l61vJ5_FOb9n6rmIeMuwQXI84JeFi0Eb-CmFP9LohKA_D_rBQRa30VoSutrEUMkNt2yWe8ojgKqFwEIA8JLky1lnRCtOMtcdO04HY7frlyrB2-ftg2Z1MM6KG7qtVdSF05I6Air8krQPSlp4U2_4C6ZphR-jCFNige7IXAEt2vnkl-8xieLT0a_iGngN7bB4Uplb-tgXBBFxcKPxq1Bl9gHakOqiEb25X_aj7HdgvGBstghoQboa9ixPAJCbcCyRi8clOrn1r5uWJZ_yMet9Tcj8cptSdFL6u0PRR-0qIrHfCxfmb4ZgA5vYhB9oV5zm3-3DrQYbEudj_lrQWfVG1904xCUmqLEttjsP9ryONxQLGT1itGDVO6w82_mHyL7YhbW1P1za8tCQ6P_PszBTTxZr1K0aoZZz8hayzaGj-4pFQjSuscMsUkZQp9g5aqYFK5f4lJuXRgy1QK3dX6t2k_A3BV4urMzmuyBvAlW1DJ99ZLS__z4AnykqXS6CB1UfFZQXaAjVOiRBcg-aUBS4VKSdKQ1lw8KTQ6E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
«ما توی جمهوری اسلامی ایران داریم خیلی خوب پیش می‌ریم. کل اونجا دیگه داغون شده.
باید کار رو تموم کنیم؛ فقط مونده تصمیم بگیریم چطوری تمومش کنیم: با راه خوب و دوستانه، یا یه راه نه‌چندان خوب!
خیلی زود می‌فهمید قراره کدوم راه رو انتخاب کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72860" target="_blank">📅 00:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72859">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423715c427.mp4?token=qbiS_fmLU-ZGdvUi1grn7yVig6JQGUPwI1Q7dZHJ3u4aXRitIcSHtwXcQYAQRwd1YC43L7gCZdjWGdTE8u0-fgcyDFBIDgzJzdNTxKB0f0qJVl3ykiJmcmYxGrRsWGc-Q7TWPoyyhARjaEVQW2s_4tKycVRbSdKfuCF7YIkO-cOGhDiuPGKDUTxCiJFHGtzs5NftrqvtBK92FyH-E21DvEp1O5yc3_X3fgQcF3v88xqXa7Hs1cRIM4sq2pzjLbVDB0fuaQ-TNAxLshOkBoDe1HKsoNcbWvXEzQ0zYNIbNbg5dEPV52Diu874XrJpXrOQBAMGo_my1TCsDC6VS1D0fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423715c427.mp4?token=qbiS_fmLU-ZGdvUi1grn7yVig6JQGUPwI1Q7dZHJ3u4aXRitIcSHtwXcQYAQRwd1YC43L7gCZdjWGdTE8u0-fgcyDFBIDgzJzdNTxKB0f0qJVl3ykiJmcmYxGrRsWGc-Q7TWPoyyhARjaEVQW2s_4tKycVRbSdKfuCF7YIkO-cOGhDiuPGKDUTxCiJFHGtzs5NftrqvtBK92FyH-E21DvEp1O5yc3_X3fgQcF3v88xqXa7Hs1cRIM4sq2pzjLbVDB0fuaQ-TNAxLshOkBoDe1HKsoNcbWvXEzQ0zYNIbNbg5dEPV52Diu874XrJpXrOQBAMGo_my1TCsDC6VS1D0fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«یادتونه خمینی رو؟ همه‌شون دیگه نیستن؛ همشون رفتن.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72859" target="_blank">📅 00:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72858">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=KvlyCdf2XvvUcPn1CP2beiBEl_H48LgxSc1HXpqaf25YHF-0Jcvgt_Ze-ANWwRbo2wXfnRcHQ_Gmr4M2ZGPhrMtcB3qKGbgdX73vTvhHYp8Vrhb9iDXU1dcLVftgW29JLv58uaiaX5z0-r6DD5KxzH-knEjciHXT8n8c7rMjkTDMXf6L4V6HNWUj55_o3o1SnC0TT7epV-ohH_US3dv5Qncw-QgqSddgcryLJrXQzqiRNk0DQrl0DAoTcn8ITPntLBhb9l5szu_gPXROl6fp2BspwwAcF6puaIyBl6XYxRXOTXAOO_iVsvwlBF4ChugyqapnEM5-_GINN522SA8fbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=KvlyCdf2XvvUcPn1CP2beiBEl_H48LgxSc1HXpqaf25YHF-0Jcvgt_Ze-ANWwRbo2wXfnRcHQ_Gmr4M2ZGPhrMtcB3qKGbgdX73vTvhHYp8Vrhb9iDXU1dcLVftgW29JLv58uaiaX5z0-r6DD5KxzH-knEjciHXT8n8c7rMjkTDMXf6L4V6HNWUj55_o3o1SnC0TT7epV-ohH_US3dv5Qncw-QgqSddgcryLJrXQzqiRNk0DQrl0DAoTcn8ITPntLBhb9l5szu_gPXROl6fp2BspwwAcF6puaIyBl6XYxRXOTXAOO_iVsvwlBF4ChugyqapnEM5-_GINN522SA8fbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:
«ده‌ها نفر از سران تروریستی ایران رو از هستی ساقط کردن و مستقیم فرستادن اون‌ور، پشت دروازه‌های جهنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72858" target="_blank">📅 00:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72857">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=tihGDgdY7I04PV2a55TWS3-I4qi4jjlkwTCD3Q9VGzhIhCluuJoKY8mhiqniFBF-s6cxfNyls3nbV3gNCToIEclLXtyp62VmGa3H_pxOt_C-LAQ9_czKWfe3vCNMpBiLLFBYKbv2744GDVOHWg2ogfAGGl07Dq65Cj3ooyiRzkhYJ-SRNljgTEZyP15mLapUB9jJEBAIoAteAHWEKPHmyFT0fTfc_698G9xVJvw6kpqTWSKv7DnYUSX7lAacf_AWUaFL9vo1E90OL6imf1MBgJjMkZRAEC6fhxeDPmkAV4a-8Qk8nl4rm5dr7PG1WPJ8Sofv-OlADv_ck53hmLnA0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=tihGDgdY7I04PV2a55TWS3-I4qi4jjlkwTCD3Q9VGzhIhCluuJoKY8mhiqniFBF-s6cxfNyls3nbV3gNCToIEclLXtyp62VmGa3H_pxOt_C-LAQ9_czKWfe3vCNMpBiLLFBYKbv2744GDVOHWg2ogfAGGl07Dq65Cj3ooyiRzkhYJ-SRNljgTEZyP15mLapUB9jJEBAIoAteAHWEKPHmyFT0fTfc_698G9xVJvw6kpqTWSKv7DnYUSX7lAacf_AWUaFL9vo1E90OL6imf1MBgJjMkZRAEC6fhxeDPmkAV4a-8Qk8nl4rm5dr7PG1WPJ8Sofv-OlADv_ck53hmLnA0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72857" target="_blank">📅 00:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72852">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/news_hut/72852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72852" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72848">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F6Jqy41fAeNq6KF1gkhilQkUrUxlUl2P7G0Y47KU9PYP29494GesBzkjbU6P5QWO566F1iD3yMNdCVepyJz2Y6opzA_gTEO42tJMcNs961lQmAFpPvgjXEdD_x0IiBl9xZFHmmgJdMd_5oA8n5SsTyMOfv0XfZsybSxeCRwQLwq0qt_GafsSv4aXZWMHTJyZw8CbwbthJY09307LXJdcU1RzNXneBPpGIXYoElrk29XJgjB3Wjs2O_1Zcbpv7wPDCkfh67R1v0dTXU3Z7saaKOfPWZ4JcJd3YGiUXBFIRIav_3nvB5b0nOd8zAmsQoaafEv6HOIJE_6JGjHJc6Xj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vTJ_8ABF0XJlzmtDvIQZ3gkac45UB9ZJte9LIjkRlwaZmFwiTMCJu4-EP6Pj7XP71eI6YiBBhYT_Z7zplI6HwQnaSTkkht5nW2PAc_Q6EuEJfT-XztSio9Qvs7ihmbLab-brkQ94xrZU_vIWh7oVoiMmebNlgwbny-JuvynlzUGqoRvcMyiejupPWu-SOP6MI6QNNLn2T9vPKKn1x3dsufwqDYxShJjlO1JBAnV0LkpZ9rkZvcq8ZdN0T3c8WEVB2b4z4G6M8Dms3EnbHkOoS44SevGMnPICxV_cGcFqAMsIN1t9DSdPuooseYis0HLz9LJQFUkyXpG5m64q19GXNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=PN6L2Pv98PB0EuanKIjIq792L-hbbK_wd7t3h1Gw4VG6L9bFRI8TogMmMi8UdS12qklCTkrqtvkdJm-mFgNwtcMKU7mhVoN9kCB25uo3t6eP3kNnoIi8-qmMwmvdB8zqC67fg9jdb9qSTlUjlI2AIVMc74Xp52TBSx-wxn_HdgjsJF_MmZK1JgqjmQWlOHbAfqTIXOXoiAuRm5vZuMjdP7ESi2CNU_vNiXUzQwBM1uKmFoU-a_Z5ZTonhWdGpsgQ3WcNWksbUhpDWnWuqpmqHj0IuMf2an694gx27YFiJ3BtUztkIkPc7VId1qyhHcWEMaIsdRfgObaG5oEhFZ3-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=PN6L2Pv98PB0EuanKIjIq792L-hbbK_wd7t3h1Gw4VG6L9bFRI8TogMmMi8UdS12qklCTkrqtvkdJm-mFgNwtcMKU7mhVoN9kCB25uo3t6eP3kNnoIi8-qmMwmvdB8zqC67fg9jdb9qSTlUjlI2AIVMc74Xp52TBSx-wxn_HdgjsJF_MmZK1JgqjmQWlOHbAfqTIXOXoiAuRm5vZuMjdP7ESi2CNU_vNiXUzQwBM1uKmFoU-a_Z5ZTonhWdGpsgQ3WcNWksbUhpDWnWuqpmqHj0IuMf2an694gx27YFiJ3BtUztkIkPc7VId1qyhHcWEMaIsdRfgObaG5oEhFZ3-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا صرافی ایرانیه «omp finix» که دارای امتیاز رسمی و تایید شده هم هست، پول مردم رو بالا کشید و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده.
مردم هم مقابل قوه قضائیه دست به اعتراضات زدن و خواستار تعیین تکلیف و پرداخت پولشون شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72848" target="_blank">📅 23:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72847">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=PWT6-z5aSH_SAFcKNvZskNGAoeU3QJfXiSY-CXoTC1o1PxkvnLbaFmxxq--TJJK_ECWfk7xcU9tRn_KVy5di6mU_nyrUlMgX6jss0KAHjC6_-vFeIsqpQuuuLJFrCdq8V7xdhT0_8hpFkgHjntX2qE6r9eMW2oAbCy1POHZtC_znDlXQKnGXCzYykrNPR2ZJJzw0QXbRsImwyfUH8en2Zkc6km9KG5O3Iyimy2eVQZ8GqGftGR7hQX7u_f0KLNz0jzdRjiw2lor96u5-UPxaRrJeh5JuYW0c8fqyWrVyplT208Lg1-HxFTL166c5scYa4zxNo1ja1P7-TKpIMQPEu0QQH8t4hSF1zP9HkvaKI4k80OZIUJ8Ms47G5A9px_s6Xs1wPWYdt4YNzir1KFLDM6qwckwxdWrLT-toX332SQj6tbls-CokytxCbFK2W3V6JFUUG4lsvAcjjwO1crwyz2ki6KRjfoWfn67m4TxWq23592Tg30CobbqNs33STCaNz67QfVPzpeMpli3vYQS7lYSbN6XX8pe9qKsnp8g7oX8N15ndHmd7b2eZDApFk2FyETxUCR3kQFy8E5A8HVc4jXF8nWGoHTDsxeBjcUp79HI52gY5wspkHbe9d2yrzZFKrxAZNVZOqRJQ1skG1lI_6nhcAenOU6zFGfcFDnSE74s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=PWT6-z5aSH_SAFcKNvZskNGAoeU3QJfXiSY-CXoTC1o1PxkvnLbaFmxxq--TJJK_ECWfk7xcU9tRn_KVy5di6mU_nyrUlMgX6jss0KAHjC6_-vFeIsqpQuuuLJFrCdq8V7xdhT0_8hpFkgHjntX2qE6r9eMW2oAbCy1POHZtC_znDlXQKnGXCzYykrNPR2ZJJzw0QXbRsImwyfUH8en2Zkc6km9KG5O3Iyimy2eVQZ8GqGftGR7hQX7u_f0KLNz0jzdRjiw2lor96u5-UPxaRrJeh5JuYW0c8fqyWrVyplT208Lg1-HxFTL166c5scYa4zxNo1ja1P7-TKpIMQPEu0QQH8t4hSF1zP9HkvaKI4k80OZIUJ8Ms47G5A9px_s6Xs1wPWYdt4YNzir1KFLDM6qwckwxdWrLT-toX332SQj6tbls-CokytxCbFK2W3V6JFUUG4lsvAcjjwO1crwyz2ki6KRjfoWfn67m4TxWq23592Tg30CobbqNs33STCaNz67QfVPzpeMpli3vYQS7lYSbN6XX8pe9qKsnp8g7oX8N15ndHmd7b2eZDApFk2FyETxUCR3kQFy8E5A8HVc4jXF8nWGoHTDsxeBjcUp79HI52gY5wspkHbe9d2yrzZFKrxAZNVZOqRJQ1skG1lI_6nhcAenOU6zFGfcFDnSE74s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار رحیمی: از امروز اگه یک سایت یا رسانه قیمت ارز (مثل دلار و یورو) رو منتشر کنه با اون سایت برخورد قانونی میشه.
جدی‌جدی اینا فکر می‌کنن با پاک کردن صورت مسئله، اصل مسئله هم پاک می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72847" target="_blank">📅 23:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72844">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=nSpliRq1AD6JolFkezWtqJ7aWQPjj-QBGOXfippmuM28qMWiFTuINsJIylhDsexHzFUVZtNB5BLbUHG3B5hHfS3-M4swH53rmjOCMRw9stZKgth28Q5aw1QWSNhNOPHWwhb3VFBGK62vlUcUHHBdbsGl0ZoVgu8-ehkJyrFNyXuHUwWi-cK82sBMeeUsOl_1JjdOx-ELXzFTqgIWVkbM1WzVou-KnDvtXrUTzcgH9Awt9Qa5GWR34_sbIwRl-omMM7SxDdbsE78ur2o5H88XD2oKbuGHCEczuaKe6nA-t9DJMb81gB5hejZNvQ3LV461v4cPVL2WW-TgiSTxbvXkOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=nSpliRq1AD6JolFkezWtqJ7aWQPjj-QBGOXfippmuM28qMWiFTuINsJIylhDsexHzFUVZtNB5BLbUHG3B5hHfS3-M4swH53rmjOCMRw9stZKgth28Q5aw1QWSNhNOPHWwhb3VFBGK62vlUcUHHBdbsGl0ZoVgu8-ehkJyrFNyXuHUwWi-cK82sBMeeUsOl_1JjdOx-ELXzFTqgIWVkbM1WzVou-KnDvtXrUTzcgH9Awt9Qa5GWR34_sbIwRl-omMM7SxDdbsE78ur2o5H88XD2oKbuGHCEczuaKe6nA-t9DJMb81gB5hejZNvQ3LV461v4cPVL2WW-TgiSTxbvXkOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ توی آب‌های نزدیک سوچی
امشب یه آتش‌سوزی گسترده توی آب‌های نزدیک سوچی روسیه راه افتاده؛
توی ویدئوها یه خط طولانی از آتیش و یه ستون خیلی بزرگ دود سیاه دیده می‌شه که از نقاط مختلف شهر هم قابل مشاهده‌ست.
حساب‌های نزدیک به اوکراین مدعی شدن این نفتکش هدف قرار گرفته، اما منابع روسی فقط گفتن یه شناور نزدیک بندر آتیش گرفته و فعلاً علت حادثه مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72844" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72843">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72843" target="_blank">📅 21:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72842">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ایران در اعتراض به برخورد دولت فرانسه با اعتراضات دانشجویی و چیزی که «نقض آشکار حقوق بشر» عنوان کرده، سفیر فرانسه در تهران رو احضار کرد!
وزارت خارجه ایران هم از فرانسه خواسته به تعهداتش در زمینه حقوق بشر پایبند باشه و آزادی‌های اساسی، به‌خصوص حق تجمع مسالمت‌آمیز، رو رعایت کنه.
جالبه رژیم جمهوری اسلامی که بویی از حقوق بشر و برخورد مسالمت‌آمیز نبرده میاد به بقیه کشورا برخورد مسالمت آمیز و رعایت حقوق بشر توصیه میکنه!
یه نکته دیگه هم که هست اینه که تا امروز هیچ گزارشی مبنی بر اینکه معترضی در فرانسه کشته شده وجود نداره و گزارش های رسمی که وجود داره نشون میده فقط بیش‌ از ۲۱۵نفر دانش‌آموز و ۸۵کادر آموزشی زخمی شدن.
از نیروهای دولتی هم حدود ۷۱۵ نفر نیروی پلیس و ژاندارم در جریان اعتراضات زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72842" target="_blank">📅 20:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72841">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw1CAi-FzIbrRIKkuS_Ow3Dfwh5PXljWdd4q5cVYXQ1FWlTbTlY2qkCmjYfpONJkDa47dJl7VlcHPYuBb5sBQ6E7nkjIks9NtbbpmDH2ir8fsZQkOS8bTeeTpoVAfHwGDVslgc2x5uCFXDF9H0abuF5WqoE6fJKGoQ5bls2x_5-Hj3Lg6aw8JxZ6ogtN7XqcKXgwda11fMQ1twHqsgF4aYxSXKnstxnFYNosMINCNHyxZq737gVU_rHIsUBP1SAZy4kq9HV6hQYlVZf_xgFGFdv8SunsJ2HmaI3xb0RK9y59MEekXw4HA4a77Xf9g4e1-39_cK6FRIV8XCXJhQo57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72841" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72840">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">#فوری
؛رایتل رسماً به مزایده گذاشته شد؛ شستا ۱۰۰ درصد سهام این اپراتور را با قیمت پایه ۱۳۰ هزار میلیارد تومان (۱۳۰ همت) برای فروش عرضه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72840" target="_blank">📅 18:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72839">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه مرد ۲۲ ساله بریتانیایی به اتهام مشکوک بودن به آماده‌سازی اقدامات تروریستی، در ارتباط با پرونده مشکوک پایگاه هوایی RAF Fairford بازداشت شده.
پلیس ضدتروریسم انگلیس گفته این فرد امروز توی وست‌مینستر لندن دستگیر شده و هفتمین نفریه که توی ارتباط با این پرونده بازداشت می‌شه؛ البته تا الان برای هیچ‌کدومشون اتهامی ثبت نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72839" target="_blank">📅 18:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72838">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=f4SLNWKiCFBhJquBFg3Q6nlxlfyPti_gPjb7eq-tZL_k-Js0fROuxFHTyKsiOSQYDVCSIpIdDk0qArJ-9bGnpdqFsPh784a9T5_Je2C5mP6jHIbyivT8q1OmVKy5gMl-ToPolXRvBXxGBWPQkxc9K8bnpDi_LGQJgyOBv8XbcRu-1U2HPTb7McwcIU-fVLgGn-252KLHgck_015Pe8paRSRsj32x4Lpp66aox73RRWoSFcDiIWGsit-1wQGRIyIzGP6-AKU5kEwtdc2-7lvhX0SLbrhxn2Ym9ONojpo1vV4ZmtjJQX45CmAX3pf18VdeDzfMAz2uWLeQ3-Ry3CCPCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=f4SLNWKiCFBhJquBFg3Q6nlxlfyPti_gPjb7eq-tZL_k-Js0fROuxFHTyKsiOSQYDVCSIpIdDk0qArJ-9bGnpdqFsPh784a9T5_Je2C5mP6jHIbyivT8q1OmVKy5gMl-ToPolXRvBXxGBWPQkxc9K8bnpDi_LGQJgyOBv8XbcRu-1U2HPTb7McwcIU-fVLgGn-252KLHgck_015Pe8paRSRsj32x4Lpp66aox73RRWoSFcDiIWGsit-1wQGRIyIzGP6-AKU5kEwtdc2-7lvhX0SLbrhxn2Ym9ONojpo1vV4ZmtjJQX45CmAX3pf18VdeDzfMAz2uWLeQ3-Ry3CCPCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون شاهد نخستین شلیک آزمایشی موشک بالستیک جدید M51.3 فرانسه از زیردریایی هسته‌ای «لو ویژیلا» بود.
مکرون:
این آزمایش، اعتبار و قدرت بازدارندگی هسته‌ای فرانسه رو نشون می‌ده:
«برای اینکه آزاد باشی، باید ازت بترسن؛ و برای اینکه ازت بترسن، باید قدرتمند باشی.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72838" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72837">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=jMaZpdXw9OCGzH4qjG8T8ONtPHI0uc34tsod8er6av4VNmQndDz-fSODTfzKp15IW-_SdiGrHDr-7B4v-UEseTKqXj8-t_fTT2qi3LGZ4UVUnRGFnB7-Ru4431feGpw-JgE6Posv9Xb-Se1982mBK2Q0M9etFNhBotKkrxMthvy3E1uOjJt0weIEqlNt67EidNOWwZcThVuv-Awjs4_bFYFLbMT8NRV7iyMPSRV9LyENZxNR1crHxsIE4jqQmDXbUof6SSKEhwVGxOL34t0dr4zIk_KJEuTod6Lqz5vXlXcTe4cwCm0XOzdUBLIHVJp4WceJH0l0HLdi7N_KDc039Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=jMaZpdXw9OCGzH4qjG8T8ONtPHI0uc34tsod8er6av4VNmQndDz-fSODTfzKp15IW-_SdiGrHDr-7B4v-UEseTKqXj8-t_fTT2qi3LGZ4UVUnRGFnB7-Ru4431feGpw-JgE6Posv9Xb-Se1982mBK2Q0M9etFNhBotKkrxMthvy3E1uOjJt0weIEqlNt67EidNOWwZcThVuv-Awjs4_bFYFLbMT8NRV7iyMPSRV9LyENZxNR1crHxsIE4jqQmDXbUof6SSKEhwVGxOL34t0dr4zIk_KJEuTod6Lqz5vXlXcTe4cwCm0XOzdUBLIHVJp4WceJH0l0HLdi7N_KDc039Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل: هر موقع میرفتم خونه و می‌دیدم کفشای لِه و درب و داغون پشت دره، می‌فهمیدم مجتبی خامنه‌ای اومده :))
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72837" target="_blank">📅 18:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72836">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72836" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72835">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKziPYrX6IjzrEuUjZBBAvfvIytHg8EhfUcEEeepC1vswuepDJIABlMX1Co6BjpAJ-Rapu1_VZjULZyNJ-GZPn_u45NH5QcLa2bi1O0o3s5WML73gqOEY3mEc4zZGfIeP9EFTjHSu_YD3g5N2cJF_jikvns6lpgp__vGbANcEudG2bmQd6c99Zj6R_j52z0qV-fDSIMTFizC_WKrGwPuVNuqWEFTxj-5fVUN1mvF2iVPOtvOPmjHLBEQsMG2RE4nNZUQYOFnfYncSPe_ZIKflc6vpV0y_twj28o0ifwiJTPDvMkhgsYK0AZtDg2fSE564-NF2olSN-uHYMv2GibxXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72835" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72834">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مارکو روبیو درباره مورد مشکوک طاعون در روسیه:
«فکر می‌کنم روسیه باید اطلاعات بیشتری رو در اختیار دنیا بذاره. کاری که باید انجام بدن همینه و امیدواریم همین کار رو بکنن.
ما هم داریم موضوع رو خیلی دقیق زیر نظر می‌گیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72834" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72833">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=EB2vLDF6YW29e077yu0b5YtSB9-LALFmsKh1hRAiW5Fx6TPmf0MGS5R8CZN9-hpIXahybyiJXyp81TUjBDQAtmvJx4OweTajH_kjz-BYElk1xJmqnRSOSnxRjqkr3ZHlc6YM1iSUZtQdtf9xyAf3LGxjUUSphCtY5At8qIbjLyqVxw2Ww3qbT3TRP0TbuIJE3t9OA8jMnLYeeH4QL-Xj5xrVwA1KWUTFSqgYAryKbnJ11HqkzSKdWHGA0nRpdmKxU7ASt7XlBJq0KDTZQGPaMGCZrcFxOe7Cnqec8gaZhtWs0rNeDJCUVLMHr00g7oaDFpY-xbmZpCt_R8at_sS4_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=EB2vLDF6YW29e077yu0b5YtSB9-LALFmsKh1hRAiW5Fx6TPmf0MGS5R8CZN9-hpIXahybyiJXyp81TUjBDQAtmvJx4OweTajH_kjz-BYElk1xJmqnRSOSnxRjqkr3ZHlc6YM1iSUZtQdtf9xyAf3LGxjUUSphCtY5At8qIbjLyqVxw2Ww3qbT3TRP0TbuIJE3t9OA8jMnLYeeH4QL-Xj5xrVwA1KWUTFSqgYAryKbnJ11HqkzSKdWHGA0nRpdmKxU7ASt7XlBJq0KDTZQGPaMGCZrcFxOe7Cnqec8gaZhtWs0rNeDJCUVLMHr00g7oaDFpY-xbmZpCt_R8at_sS4_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی : مردم ایران در دنیای واقعی خیلی خوشحال و شاد هستن ، واکنش ها تو فضای مجازی دروغ هس و حقیقت نداره
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72833" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
