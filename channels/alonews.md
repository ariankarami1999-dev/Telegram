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
<img src="https://cdn4.telesco.pe/file/qLhLmHA8OLXraenVcJUmytpExJKMH8newebthXSX8tIjEnzP6QW2pU2pOHXKeYM_l8-IbnaqMArVnH779FbVc-358vSHVVto8dXiOJpE9FiHoUiHC8mLwHnct6KT1x9GnwGogZBTHXIBjGi0qHDQtdcKq0-VKRjbgMJgs7u6Oj-SYmp-nSvQT6Pn11h2Dfx_QS8y-Er9pPr_Oi2-cIDz9vQAgH2iPa0byVHs9H0xgTAv8TCNybYDNNhQhMagss1hK810mOOzMJr09dChbMSpVcBmGJc51nzAPTlN8lTg5ol9IijeO9rP-exxzT6c_Hs3vk-2KJ7555Xl7Mwb-DgWng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 970K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 19:05:31</div>
<hr>

<div class="tg-post" id="msg-148226">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">ویدیو وایرال شده از ارزش پول ایران
ادم نمیدونه بخنده یا گریه کنه..
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/148226" target="_blank">📅 19:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148225">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فیلد مارشال رضایی: برآوردها و محاسبات رئیس جمهور آمریکا در مورد ایران اشتباه بوده و جنگ توسط نتانیاهو آغاز شده است.‌‌
🔴
به نفع واشنگتن است که شرایط ما برای خروج از جنگ را بپذیرد و تهدیدهای ترامپ نتیجه ای نخواهد داشت و ما آماده یک جنگ سرنوشت ساز هستیم.‌‌
🔴
ما نقاط ضعف ارتش آمریکا را می دانیم و بیش از گذشته برای مقابله با حملات هوایی آن آمادگی داریم.‌‌
🔴
به این باور رسیده ایم که استراتژی خود را در قبال واشنگتن پس از خروج از یادداشت تفاهم تغییر دهیم.‌‌
🔴
اخیراً یک موشک ضد کشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کردیم.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/148225" target="_blank">📅 18:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148224">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی پادشاهی عربستان به مواضع انصارالله/حوثی در جبهه شرقی تعز، یمن غربی.
🔴
این جنگنده‌های نیروی هوایی عربستان از پایگاه هوایی ملک فهد در طائف، عربستان غربی، به پرواز درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/148224" target="_blank">📅 18:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148223">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ: برای پیروزی، به رهبران کشنده‌ای نیاز داریم که بدانند چگونه پیروز شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/148223" target="_blank">📅 18:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148222">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6cbcc478.mp4?token=XEc0Hx66khmALQc1lKH0E227CSAgJao6me2tuxlbZMjUfa6wdIFnaoWId6Fs3oH-KdtERPxx_xS0bb64ykbQMQWH4chS5cZEkdDRDJ-gVeFGxd1PpMukwmThc4LXrCj_FwCTucnW_gy3fJl46x_KzJ5uAAGsMXQBsYrs91G5xTtHTcAmUlanZdSasnuLUEXl4q_8jDOuopTl-OSY9BpVle_Yfjgn_yxAC758w-AxxglAjUirD-JZjjp0WVMoRWAsIY6oytkXTt4krTkb1KK7V3FckmQEOBbhrNT65PO1FE8lLJ8-r51AeT8TJvfxE9l4Jyvsa45uHV9yP_z65Mdgrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6cbcc478.mp4?token=XEc0Hx66khmALQc1lKH0E227CSAgJao6me2tuxlbZMjUfa6wdIFnaoWId6Fs3oH-KdtERPxx_xS0bb64ykbQMQWH4chS5cZEkdDRDJ-gVeFGxd1PpMukwmThc4LXrCj_FwCTucnW_gy3fJl46x_KzJ5uAAGsMXQBsYrs91G5xTtHTcAmUlanZdSasnuLUEXl4q_8jDOuopTl-OSY9BpVle_Yfjgn_yxAC758w-AxxglAjUirD-JZjjp0WVMoRWAsIY6oytkXTt4krTkb1KK7V3FckmQEOBbhrNT65PO1FE8lLJ8-r51AeT8TJvfxE9l4Jyvsa45uHV9yP_z65Mdgrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت
هگستث، وزیر جنگ:
برای پیروزی، به رهبران کشنده‌ای نیاز داریم که بدانند چگونه پیروز شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/148222" target="_blank">📅 18:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148220">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dbc95860.mp4?token=NOJF5fhmNA4rJ5VnD0zfS1UhedwBTJyeEIQD7e2-jmaK0ej6EgPbK7GL4gPCzIcsJfGpePe49rbpCzc_64e_ZsmoSuEEPV1y4JVJCh_aZOQ7i7I8lSlEjw3KcAXeTL_I3cEGqBrwHZrCGIM121C7Mm1q6DlQv_SxJyA1aIkf0keEJSBGOUc5SFUSnShUMwQyHVY1dWtb4BB4EUqM9kRehnaIzwFRcxM6zoYSLRKD4aBgxSDbj98rDi8l1N-Iy0h7Y8ppOZ8PvWTFv-zQeU58fddzvItYOVGeX_DuOYhvusTSlcQEUOH06Z2UkGhguGnC6Xxm_h2C8CrjhvxYyQ3Hlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dbc95860.mp4?token=NOJF5fhmNA4rJ5VnD0zfS1UhedwBTJyeEIQD7e2-jmaK0ej6EgPbK7GL4gPCzIcsJfGpePe49rbpCzc_64e_ZsmoSuEEPV1y4JVJCh_aZOQ7i7I8lSlEjw3KcAXeTL_I3cEGqBrwHZrCGIM121C7Mm1q6DlQv_SxJyA1aIkf0keEJSBGOUc5SFUSnShUMwQyHVY1dWtb4BB4EUqM9kRehnaIzwFRcxM6zoYSLRKD4aBgxSDbj98rDi8l1N-Iy0h7Y8ppOZ8PvWTFv-zQeU58fddzvItYOVGeX_DuOYhvusTSlcQEUOH06Z2UkGhguGnC6Xxm_h2C8CrjhvxYyQ3Hlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث وزیر جنگ:
اگر ارتش ایالات متحده آمریکا رو به چالش بکشید، شکست پایان شما خواهد بود.
🔴
در دوران ترامپ، جهان آموخته است که ما فقط برای پیروزی می‌جنگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/148220" target="_blank">📅 18:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148219">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54da84d255.mp4?token=CLY3OfZ0fjGiBcPbPkebuLn9_fm8rWrRn4qPB_s9JwMwi9j-GtuJcy9SWz-67RtU-86X4L0IOIcdRQTgF29ch_JnT5PjatRokm4rGns9DI5LBGbl5Y-HiG-rioMDKuIqWPgA2mmCjgTcyFNK2zJ1A0i2wFdbBjnk2Iwcc77IKsgsMmZR9Xo-GWydSZaIXEbk8OGvMbn1jmZRXadzoppnU0I8f25E2Ows_aVderXfYXNULJOQI3o2Dmn3iV1t3QyH-x2qu_HCci0_07Dw9UJpNi7JoMciMQir1GqUbyVHE-xw7frPxCkzZM2uNRJIDvwDYjVUdurIIXAA3UuwXuoZnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54da84d255.mp4?token=CLY3OfZ0fjGiBcPbPkebuLn9_fm8rWrRn4qPB_s9JwMwi9j-GtuJcy9SWz-67RtU-86X4L0IOIcdRQTgF29ch_JnT5PjatRokm4rGns9DI5LBGbl5Y-HiG-rioMDKuIqWPgA2mmCjgTcyFNK2zJ1A0i2wFdbBjnk2Iwcc77IKsgsMmZR9Xo-GWydSZaIXEbk8OGvMbn1jmZRXadzoppnU0I8f25E2Ows_aVderXfYXNULJOQI3o2Dmn3iV1t3QyH-x2qu_HCci0_07Dw9UJpNi7JoMciMQir1GqUbyVHE-xw7frPxCkzZM2uNRJIDvwDYjVUdurIIXAA3UuwXuoZnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: من جای ایران باشم، دنبال ارتباط مستمر با ونس می‌روم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/148219" target="_blank">📅 18:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148218">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5phdGSj23PJrjOPCq-D24XozCv70VQLv81W17uDMJUnSRlVGJxmwXYDXovSWs4vfo48VwSZcr5yxZDyS5sS-H0aUMn7iLOqAs1SFJfORlSYSrQxyh2gDxP7GUn9OclH93dJOnf3ekq4Gf7x7FIUXW8c76M2mK0hwvq_OrJJVZf_XKir27jdSBCNKDD-6cmABp1ZPYMhcqLH2zMdLFbK33EEuHQ-v29a4ZpR-la9piu-iXwO8VC_sBTxSkwI5vBQSk4onue_3tLcnjhmu2QaRE4QDPTC9sIOmBcL2puEBZqpYbyJmBXL9XfQFuvdbFKSspTCtrGnZi67Q5Z--98LwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی تراستی‌ها برای افزایش سهم محموله‌هایشان، کشتی‌های رقبا را لو میدادند تا توقیف بشوند…
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/148218" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148217">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=T6dGIwHWmt_vaA9DzmFWXcrTvEP0cD-WYD_VeF0n8be2N1WHPJnLJkgXHxCw6xH1esXzJxEHx0dURiSQUDQta4XOvs9q78hszZF-2XQUgINBcNAqq3v-vnNLO4C1FLsuAC4mFNAP-1EvFBApcinbDovmsFbVSuyavEh1odPKJujjYI51w5sBehYwyNnlOm8QNW-LlbIzGD63GIIeOP38cimjbSwmwEpcYlSjFwxVu_G8wnlsGbjSjJpxBZqJvwvXVMYLprayijpgGmq8oxaAFvftUKK-WocgJek8Fj31djZMNMgqOyngUF4wbaSSxazzNXFOEOwZDYX6_q-tQSoKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=T6dGIwHWmt_vaA9DzmFWXcrTvEP0cD-WYD_VeF0n8be2N1WHPJnLJkgXHxCw6xH1esXzJxEHx0dURiSQUDQta4XOvs9q78hszZF-2XQUgINBcNAqq3v-vnNLO4C1FLsuAC4mFNAP-1EvFBApcinbDovmsFbVSuyavEh1odPKJujjYI51w5sBehYwyNnlOm8QNW-LlbIzGD63GIIeOP38cimjbSwmwEpcYlSjFwxVu_G8wnlsGbjSjJpxBZqJvwvXVMYLprayijpgGmq8oxaAFvftUKK-WocgJek8Fj31djZMNMgqOyngUF4wbaSSxazzNXFOEOwZDYX6_q-tQSoKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی به تخریب در مناطق مایس الجبل و المنصوری در جنوب لبنان ادامه می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/148217" target="_blank">📅 17:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148216">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
حسین پوراکبریان، عکاس و طبیعت‌گرد، تصاویری از پرواز صدها فلامینگو بر فراز دریاچه مهارلو در استان فارس منتشر کرد و در توضیح این تصاویر، با اشاره به گسترش نمک و فاضلاب، نسبت به وضعیت زیستگاه فلامینگوها ابراز نگرانی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/148216" target="_blank">📅 17:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148215">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رئیس‌جمهور لهستان: پوتین در حال برنامه‌ریزی برای حمله به کشورهایی حامی اوکراین است تا اراده ناتو را فلج کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148215" target="_blank">📅 17:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148214">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148214" target="_blank">📅 16:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148213">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d70147ef.mp4?token=mOj61g0KHkRZH8TJRK5fISL4S19x-ZbOIC4VPGgmEOSrNAowLxjq1Sz2hjD9IFLrnhbwb1dgOIsghV8ifVJaEkHznzErrKeL3q1tqq4w4L4880rKpVc3j7wU536rTlgAmqIvPN1G75KNBxGcgtkGFk9mppGFawel9aEsWVkKfOo8VWGGTyYviKDmZ0f3pSFgowzDPRqVUXvBtfNX36Dy7-TJkjbewu0XUYwHUwnyY5hBeTc0Jn8_W0G1B48AfPAOwUCmFwEBh7UutG0FWTqbk0HmPM8pY3KffSm1TJ6KXXs61e3WHxiyzyNaJycWwkAr1yYRjU9EC0Q9cRY8oT3fxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d70147ef.mp4?token=mOj61g0KHkRZH8TJRK5fISL4S19x-ZbOIC4VPGgmEOSrNAowLxjq1Sz2hjD9IFLrnhbwb1dgOIsghV8ifVJaEkHznzErrKeL3q1tqq4w4L4880rKpVc3j7wU536rTlgAmqIvPN1G75KNBxGcgtkGFk9mppGFawel9aEsWVkKfOo8VWGGTyYviKDmZ0f3pSFgowzDPRqVUXvBtfNX36Dy7-TJkjbewu0XUYwHUwnyY5hBeTc0Jn8_W0G1B48AfPAOwUCmFwEBh7UutG0FWTqbk0HmPM8pY3KffSm1TJ6KXXs61e3WHxiyzyNaJycWwkAr1yYRjU9EC0Q9cRY8oT3fxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جوزپه کاوو دراگونه، رئیس ستاد نظامی ناتو: در مورد فعالیت‌های ترکیبی، درخواست خودکار ماده ۵ (معاهده ناتو) مطرح نمی‌شود، زیرا معمولاً این فعالیت‌ها از آستانه بحرانی پایین‌تر هستند.
🔴
منظورم این است که یک حمله مستقیم در دستور کار نیست. اما یک حمله مستقیم، به طور کلی، فوراً منجر به درخواست ماده ۵ خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148213" target="_blank">📅 16:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148212">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148212" target="_blank">📅 16:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148211">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
کمیسیون امنیت‌ملی: کاری کردیم که آمریکاییا دخل و خرجشون دیگه نمیخونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/148211" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148210">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده: ما با دیدی روشن و تمرکز کامل در کنار همکاران خود در سازمان‌های مختلف دولتی ایالات متحده، همچنین با تمامی شرکای عضو شورای همکاری خلیج فارس، و همچنین شرکت‌های بیمه و حمل‌ونقل، برای افزایش حجم تردد از تنگه…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148210" target="_blank">📅 16:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148209">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده: ما با دیدی روشن و تمرکز کامل در کنار همکاران خود در سازمان‌های مختلف دولتی ایالات متحده، همچنین با تمامی شرکای عضو شورای همکاری خلیج فارس، و همچنین شرکت‌های بیمه و حمل‌ونقل، برای افزایش حجم تردد از تنگه هرمز همکاری می‌کنیم.
🔴
این تلاش‌ها نتیجه‌بخش بوده است. حجم نفت خام، بار و گاز طبیعی مایع در دو هفته گذشته، بیشتر از هر زمان دیگری در شش ماه گذشته بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148209" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148208">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ژنرال برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (CENTCOM):
نیروهای CENTCOM در ماه‌های اخیر، انتقال بیش از یک میلیارد بشکه نفت خام از خلیج فارس از طریق تنگه هرمز را پشتیبانی کرده‌اند
🔴
ما به این دستاورد مهم دست یافته‌ایم، در حالی که با ارائه حفاظت هماهنگ، به عبور بیش از 2000 کشتی تجاری از این تنگه کمک کرده‌ایم.
🔴
مسیرهای اصلی عبور در این تنگه از مین‌ها پاکسازی شده‌اند. هزاران کشتی از این تنگه عبور کرده‌اند.
🔴
بیش از یک میلیارد بشکه نفت خام از طریق تنگه هرمز از سوی کشورهای هم‌پیمان خلیج فارس صادر شده است، و ایران به دلیل محاصره قاطع ما، هیچ بشکه‌ای صادر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/148208" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148207">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12d9906e4.mp4?token=Rvt51IR2mflpXuZyhZ2MM74BjCTPCyPtL0sUF32aBp9r_fQHIgxyyHXycTcJkHGKV-ssIb7qTDfg_LCEJqM4VFkSQmq__FNJRtGN5R--v_eyQOY8eEikQL7URDYuMX8BbLIYBWwA4uUI9AMzo4ro_p-7OQ80JzkCvk5XIwaelXK7Tcd2K2R7QMfHxtpwacz9XK3sDZjKADLe4nqt_WrGN3EhXgmU7QS72YZ022IadSpIGhEgAmi2LzCxDnAVVutkl-sChBuADp0C5LzGaEc2Xr-mWDQqRFD8nmm7eQpZXNWQl-j30PfBYhPmX_MRRMchufw9UlbS636ieVZoOeupXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12d9906e4.mp4?token=Rvt51IR2mflpXuZyhZ2MM74BjCTPCyPtL0sUF32aBp9r_fQHIgxyyHXycTcJkHGKV-ssIb7qTDfg_LCEJqM4VFkSQmq__FNJRtGN5R--v_eyQOY8eEikQL7URDYuMX8BbLIYBWwA4uUI9AMzo4ro_p-7OQ80JzkCvk5XIwaelXK7Tcd2K2R7QMfHxtpwacz9XK3sDZjKADLe4nqt_WrGN3EhXgmU7QS72YZ022IadSpIGhEgAmi2LzCxDnAVVutkl-sChBuADp0C5LzGaEc2Xr-mWDQqRFD8nmm7eQpZXNWQl-j30PfBYhPmX_MRRMchufw9UlbS636ieVZoOeupXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محل وقوع آتش‌سوزی در فرودگاه ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148207" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148206">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
هیمتی: چرخ اقتصاد کشور فعال شده و اوضاع درحال تثبیت شدنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/148206" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148205">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgxHSwA9IX0jEjxpQcCIlswjN-ZpfkqZcSAwxu1uQj3JAb57-1prXBBUpSQJAeGFWXeZ2bps7td3gyji2Y_RW7lM5SRp-mXvjJfk2gV4ln9pRI4ePqLW7mQKIgpkbGvChpZsvyyhdnhd3Qv8i_73Wx4PZ7KnWY4sSd6YEtwCnAk8WHUY-znenIeGv-8Eb1cbV8CxFvggeYj0Ot2G84oDiv1jjZWjLRz6x0JWrXx3gS7L4T7IxZjB31hH6lXXtN9NAfDcqiJevCO3M6Txx0St5L_PfWnD8bFZ2_e5cVQRmQiF6oiaydJ8aZfaYEcVS5egxWpzCuBxDdeOY0xsgJ485g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاسبی جدید با نوبت گیری دکتر: ۲۳۰ هزار تومان بده وقت بگیریم!
🔴
نوبت‌گیری پزشک و دندان‌پزشک حالا برای برخی افراد به یک منبع درآمد تبدیل شده است. برخی بابت این خدمات بین ۵۰ تا ۲۳۰ هزار تومان دریافت می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148205" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148204">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7383ac988.mp4?token=OLk1-GF1NfG5rFLjGucjhuw2EZSLId5KB7F-eWSw1tvsQ2AAMMqgp13ceFcPEQH4bjtEQxcdPmtW332DcXWh6ZCyvhrB_Yn7iJH4cv1YvSpi7TEp92Qz8vh_G-K80IvWzubwH6LVtxxgSEGgGTUQR9nRRc9avZcvbTQdEnXBfWnWKeftF_AwU4z3He-cKb_C00VeqWgAz5U2GmuKCc3JqZWxFdKAI1mJBm7BGdv_7ySa-bKhP8jvQkz9hUCutr5gsc5HXT4XJawoUtd2yhSKfFHQzRsVdxDcuT2OQmpTQHFsDqaX3Ua-as6xcyJqZAHGAaCVyfnhUdvKiqBNlUIPoILjEeVoVjpx7L8jfy7UxjClC7K4oFYvvE_vRzeujMPN5VddEj_ERDLEKfDm7qzZ8ngTUHWhxVd833qHtW5MJDLGpC1WJfs1ZFV81Jm20gw9v-yUJtkw2ut2mCMtvxoyCF6eZz0dhOLPU641HHztZKA-rlB_WQC0mfb79aNpAoUb1aegpI78GfA9D6BGLNtaBsIiaH3S9rdV-9CfmEjxFfmLcaDPsLIQ0QoO3eHQNd0WHqwKngHl2ZdgeimpaBCPg0TYy_zOBTIvYM6xiZS4ZLG1aHgJsw0yzYLoFRJQcVwiTMOhhuusFyUfR0MgZdUJ_AKEUk4I8JDEpVfLEQ4s5Ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7383ac988.mp4?token=OLk1-GF1NfG5rFLjGucjhuw2EZSLId5KB7F-eWSw1tvsQ2AAMMqgp13ceFcPEQH4bjtEQxcdPmtW332DcXWh6ZCyvhrB_Yn7iJH4cv1YvSpi7TEp92Qz8vh_G-K80IvWzubwH6LVtxxgSEGgGTUQR9nRRc9avZcvbTQdEnXBfWnWKeftF_AwU4z3He-cKb_C00VeqWgAz5U2GmuKCc3JqZWxFdKAI1mJBm7BGdv_7ySa-bKhP8jvQkz9hUCutr5gsc5HXT4XJawoUtd2yhSKfFHQzRsVdxDcuT2OQmpTQHFsDqaX3Ua-as6xcyJqZAHGAaCVyfnhUdvKiqBNlUIPoILjEeVoVjpx7L8jfy7UxjClC7K4oFYvvE_vRzeujMPN5VddEj_ERDLEKfDm7qzZ8ngTUHWhxVd833qHtW5MJDLGpC1WJfs1ZFV81Jm20gw9v-yUJtkw2ut2mCMtvxoyCF6eZz0dhOLPU641HHztZKA-rlB_WQC0mfb79aNpAoUb1aegpI78GfA9D6BGLNtaBsIiaH3S9rdV-9CfmEjxFfmLcaDPsLIQ0QoO3eHQNd0WHqwKngHl2ZdgeimpaBCPg0TYy_zOBTIvYM6xiZS4ZLG1aHgJsw0yzYLoFRJQcVwiTMOhhuusFyUfR0MgZdUJ_AKEUk4I8JDEpVfLEQ4s5Ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بوریس جانسون: به نظرم این استدلال که روسیه به‌نوعی به‌خاطر استقلال اوکراین چیزی را از دست داده، کاملاً اشتباه است. داشتن یک همسایه آزاد و مرفه چه ضرری برای روسیه دارد؟
🔴
اما درباره اینکه چرا این موضوع مشخصاً برای پوتین اهمیت دارد، پاسخی وجود دارد. پوتین می‌خواهد یک الگوی سیاسی خاص را حفظ کند. او دموکراسی نمی‌خواهد و اوکراین آینده‌ای جایگزین را برای روسیه به نمایش می‌گذارد: کشوری آزاد، مطبوعات آزاد، جامعه‌ای کثرت‌گرا و رسانه‌های آزاد.
🔴
او از این متنفر است. مشکل همین است. تهدید علیه ایدئولوژی او، خودِ اوکراین نیست؛ بلکه اوکراینِ آزاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148204" target="_blank">📅 16:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148203">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سوئیس کشوری که ۲۰۰سال توهیچ جنگی نبوده و نماد بی طرفیه وضعیت جنگی اعلام میکنه !
🔴
با این اعلام آمادگی برای شرایط اضطراری که اکثر دولت های اروپایی دارن اعلام میکنن به احتمال بالا روسیه قراره علیه ناتو اقدامی انجام بده ‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148203" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148202">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byVGAQOnF57Glx5iFCzo3u1hZi72Lu-G4KFrFhn7x6B1DdCpdu8dli4A-subu5ST0qe7YQ2fyXmNjcI5AgNsHzuNkvgAOo18pB9B1wvy9CgFOrINvwfneiW-C5yx7X0QhFuw1TH9uIeINxwsbu6O2aVY2zEzCrnuQRE81XkiE6NfX0D4nKbWHf37OaiD9eqY9qOtCCsL8d6F2SOcSzZSKKkuBhXnVkSx4n1YMpL9g_v37GKTtyIVx0Ed_XW2M3WrEW5OPFGw7-JdEZfX4OSZooCeUBm8yXr8uPS1V_vC_EDAGvEZg9Xag5SpN9ywamZfbwmI5LukxEpolub0Bw60hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوئیس کشوری که ۲۰۰سال توهیچ جنگی نبوده و نماد بی طرفیه وضعیت جنگی اعلام میکنه !
🔴
با این اعلام آمادگی برای شرایط اضطراری که اکثر دولت های اروپایی دارن اعلام میکنن به احتمال بالا روسیه قراره علیه ناتو اقدامی انجام بده
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148202" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148201">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7509fa857.mp4?token=uLWTYXmn62iPaHX-LHpEZKJHKTZnFsRfhIja1oMckNg94B-gtlY1OPCxBVfBAojcxOQR2MPNo83lt-PRYaoT8hA5YhmwFlQ5qinp71EEn96DuZEpNswcTJYBqiB4nJtvE4GDGu_sUDm1HOI3xO-jWvdACOOmEmY5h6u4HAN3BEAvE0m57KKgtCo4t0tgQZ8zBvumqmF_itpA2l8JYv3K7JmMwOZcypgOSOX27vUB7X2e7mUmwv8sAPM07nNoZU279YvbdAnTMOY_j2phP0-Lsxp4u6tiu1ADFlHW2dA69_wvO6D9gsbC8pEy0ErOl3niySZWRZSuJHPBRHoEJIzmjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7509fa857.mp4?token=uLWTYXmn62iPaHX-LHpEZKJHKTZnFsRfhIja1oMckNg94B-gtlY1OPCxBVfBAojcxOQR2MPNo83lt-PRYaoT8hA5YhmwFlQ5qinp71EEn96DuZEpNswcTJYBqiB4nJtvE4GDGu_sUDm1HOI3xO-jWvdACOOmEmY5h6u4HAN3BEAvE0m57KKgtCo4t0tgQZ8zBvumqmF_itpA2l8JYv3K7JmMwOZcypgOSOX27vUB7X2e7mUmwv8sAPM07nNoZU279YvbdAnTMOY_j2phP0-Lsxp4u6tiu1ADFlHW2dA69_wvO6D9gsbC8pEy0ErOl3niySZWRZSuJHPBRHoEJIzmjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای از فعال شدن سامان‌های پدافند هوایی در ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148201" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148200">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdydG2JEtShHlvqksmCSRokkOcVklqXoXE-p9zAzcj3qchnGCS1H8vPjC0aeu1bg1-O6QGEUhDJ0OqLUgyIHAo345RV2N4fo83NgSeZHG_Mc0Pq6LeypgjqdrccBn8I7E9q0U848Kx_IPFatmDSzgCk0f1rJPVgdf4LmDlcQlkuUJec7wwpVbibYxBG6-2kUPbieFcsVnW2KmcHyJgMAh88ppJO9ROAMFEAo3p84tzgq5pPHEkXgLp3vzwIpeXE7CYg9SQKCSoXbwCutBy36CcECNpCPkmga-B3K6_5nireEU_3vXnpQDmAfqfCNHmNgExJyae6zsMLpWh1fymoLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواشناسی: شدت بارش باران و برف در مهر و آبان ماه به حدی شدید خواهد بود که در اکثر استانهای کشور احتمال سیل و کولاک وجود داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148200" target="_blank">📅 15:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148196">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kfg02F2bEafQsyZjTgUyfruNwZX0OXy0CmXBSD4hYxNmZbYuf5x8lmnNJDmQriwwytInRRYcyBN8WlHjbM604q8UrBtbZ-3hel7_T0Uzzvbz3twpN3Noum0dgfxwwmNSK5bkieiVUaaLiwQTBO53QjdbAYL_fC5xPWPtP2lgV_9FWVad_IIa-KfVnAKjACBiBZblzYNgt49Z2XL6MQJsH4rzxxg7-4VF5xxq2cyWy1wtTGtkMkrI3vCJVkk6Y2yiO5P_uKIt6NDMItCG4OhtkvQPM0etBHD4Ny6xBuCGG1SmeQlzuViOKozYTppUUCUe1SZ-EeAbKpv5TVqQQ96rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t6GyKghOvZUV0QZNQI3LnsvYK6lk2VkOxeU8Hy3HCK51wHe7UfR6CN1-a5YuZocZ8E7OCPQ-28OJ6GxD5RTC7OVr1LRl4r97amnAMNfnfB4VZUHRdz0sBn2xfFKbsj_3v_SGolHei2qyo4u0CYaL-xfYkLxhfW2jHMJX480RCOSvgYiqGrZWMoyuBMj4HtcM_Q9oqECyJTX2QyWy7ddW0bKbuarMajj5fmJBc8jhKRzscOQn_PXHBXMrxXfjp1ueKYesOCpEbetQlI8KxkffV1hO6GBr6MjS2FlLUr-_ByBnxbs_KUrY3E8hzSVSUxBbjuNZLWzC05EgReyyVIl_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FCY6mCBEwLDjQMKnOry_FAphwlhow5keTZ6mZeiyMlkPETcBzM9jC643ucOs3YA5wH03HS1phn6W2cogxNvklPdMWBHtpCzicsMNA4rV4l8jLoOVFiQsnEiQApjlKT6RVKchVwtUolKP6jey89-STllc0XyRIvwUs8LKQGSEJb1uoDZU85I2p7TwTNAZsM1wwkkGqtwo4BV09nNARb8m1Xe70_7N3A9mRuWauZm9PMO68NSuwx9XhkhUN5UF3iSzN-_sF1ZoDay0sMSLCoXt5kvyPt6LcKI8FdJApwkrbP5g4m6lri5a5FcmRB26Oufc3OMQEKV9tiAMBse931kYqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RHpe0XHRbSIY-wMVDwM1U9l5IU8cPJUibLkJkkz1k68R9VqMv64vJ5gqHCHdJKXvj0d_HJP1aMrbCSZEB2O_7QrEwzFz2cVJBV0a2cLEv3IvufBj6g9JouH1PPQEfq9aZo-NpG8NkJOMkN9uMlHyVgU7cq71tlMEev-8N4M8Ar3i0T90BQVO_yF2rgaJsqkEpMrrNBQOrw8QoDBqVM_Mqqb1Jo4DqeKQI_T55LSrG4HmDaKmjQG4AzFuGCJpVq_1xHJMaExlEkWcOOLOCxb3u-WnCgAhl3mAV5DaMx0-KtFBwlJXdj7WwVxx9w8fmaYzRaGyjBya9y4fvEgKALszmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جزیره فارو اعلام کرده که مهاجر می‌پذیره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148196" target="_blank">📅 15:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148194">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243abf4097.mp4?token=ag2JU_pJaqiL8cyjCX4ua_ogufhatT3OxHQOWCFAkA58qjsUiBpaRWGLI9jC-6VsfASnmHUoq7_qhVG_Xv0CXalg2Vv1PZfYMAg5yvdS-ZN-rSmXWxgLYsKmRtOC0Jc3LU1QE_fic10WxoagsrTwtg7r_pupN3DIcuUVCpQmSZ_6SE8nk9wTPiHX6DeCR2Mc3bfOncXWDbQrjpYkKDsdbqpsAkn_f3gKk7VJnBsHKMDL0hkWvfi9Mr_quT0Y0Y6o43cPCokxDECktuAEGZkuJUisTTn3bIKxzDeIucLh5Iz4ajJgBzy8wXzrLwLpZXFe294uxkMypVK9LUrqk8r1YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243abf4097.mp4?token=ag2JU_pJaqiL8cyjCX4ua_ogufhatT3OxHQOWCFAkA58qjsUiBpaRWGLI9jC-6VsfASnmHUoq7_qhVG_Xv0CXalg2Vv1PZfYMAg5yvdS-ZN-rSmXWxgLYsKmRtOC0Jc3LU1QE_fic10WxoagsrTwtg7r_pupN3DIcuUVCpQmSZ_6SE8nk9wTPiHX6DeCR2Mc3bfOncXWDbQrjpYkKDsdbqpsAkn_f3gKk7VJnBsHKMDL0hkWvfi9Mr_quT0Y0Y6o43cPCokxDECktuAEGZkuJUisTTn3bIKxzDeIucLh5Iz4ajJgBzy8wXzrLwLpZXFe294uxkMypVK9LUrqk8r1YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قار قار کردن و توهین عده‌ای به پزشکیان در دورهمی دیروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148194" target="_blank">📅 15:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148193">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
پوتین: رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148193" target="_blank">📅 15:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148192">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
یاشار سلطانی: کشور صاحاب نداره! رئیس جمهور و رئیس مجلس یه توافق رو انجام دادن اما عده ای خودسر موشک شلیک کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148192" target="_blank">📅 15:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148191">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یاشار سلطانی: کشور صاحاب نداره! رئیس جمهور و رئیس مجلس یه توافق رو انجام دادن اما عده ای خودسر موشک شلیک کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148191" target="_blank">📅 15:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148190">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مکرون: خواهان بازگشایی تنگه هرمز از طریق دیپلماسی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148190" target="_blank">📅 15:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148189">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
واردات خودرو مدل ۲۰۲۳ آزاد شد
🔴
تا پیش از این، تنها خودروهای مدل ۲۰۲۱ و ۲۰۲۲ در این رویه امکان ثبت سفارش داشتند، اما مدل‌های ۲۰۲۳ نیز اکنون به این فهرست اضافه شده‌اند. جزئیات شرایط جدید و الزامات قانونی، همچنان اهمیت زیادی برای متقاضیان دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148189" target="_blank">📅 15:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148186">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na3IE3hV-dioG2DJDj1d2Yn1aNCq8xtEiN4cgTSxf0MSQvuDE_gyKsyTa33VcKDHprGT40149XhWRxnkAMN46jWTFAa1PSfMTESrdbSVhaz8u3Sf6MFSMTSPAakB6ZsVmhgTavf4w65lQ7cGluRenRDzcq0AHHoxl_pnbU3fBGieRM6yR-sAA0m5Ams0wvIzVBR0rwTOnW2Ufqh_Q92JbysOfShErvTWq8xyWnk6QCpBDNllzzMUhPoRFL8RxELNX2WlHaPaGM8MtBI0ZSsRMKW84ll-dStmBjW-zIU4IUOKQt0cC4d2sxs9FphcweyLzk9iMmYb7aHPZ5DLUM8hDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a4c429f9.mp4?token=aD03XEajy-a6-9u_uEu0n9aUQmwh4VRAIjWzzN-3wHLvO8lB4rskYYMgxFk6sHVqiA2vg2pChY4v2sBnBII_72Aap53E0itzZH4OaW9395ncKepPLtqZ0WwowWl3MS5-NTmJLAJcsl62odnPnLnYdJYeZv4I86Vj-fyDoPj9S787skHEvCYLgM3hohRx81RdQ6JWIMi6ic0lcWBBliSUJmtlkuYSzY1cntRp7irrha-hZ5PelxhUipVM7tYpzilr2q_nmO4WjYJYfXZ2fP9NFZl_PhSJJgf4XxIwbJZQ7COAZ_YGWp_MXnJUIpyuwCcFh8IOk9jkRtzfkQf4BoPTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a4c429f9.mp4?token=aD03XEajy-a6-9u_uEu0n9aUQmwh4VRAIjWzzN-3wHLvO8lB4rskYYMgxFk6sHVqiA2vg2pChY4v2sBnBII_72Aap53E0itzZH4OaW9395ncKepPLtqZ0WwowWl3MS5-NTmJLAJcsl62odnPnLnYdJYeZv4I86Vj-fyDoPj9S787skHEvCYLgM3hohRx81RdQ6JWIMi6ic0lcWBBliSUJmtlkuYSzY1cntRp7irrha-hZ5PelxhUipVM7tYpzilr2q_nmO4WjYJYfXZ2fP9NFZl_PhSJJgf4XxIwbJZQ7COAZ_YGWp_MXnJUIpyuwCcFh8IOk9jkRtzfkQf4BoPTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیگر از انبار ذخیره سوخت در فرودگاه بین‌المللی شاه خالد در ریاض، عربستان سعودی که در حال سوختن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/148186" target="_blank">📅 15:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148185">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd3300290.mp4?token=t-ejjACXnsSyyHKDCyEncZAqgYUe2ycHUL4cygvXQ7p2S6LvvFQsT-sOfvE2Ea78-B8yaxXP2yCrJsb8eRrjAVtYu6iIodxCLWW2y5Qoi5Z6buknOOuRUnzWD18iKspLoDF6lz2RH7gZWa5t6VuoufavU2xRjgZ3XaRfChf2Ajzg9XE10kP6oqtwgjPx7Sn2Bfbo1urtexxhDJnW0bPLLFA1ASPSPRSrvnq8n24_K9wqyOiitZ5x2VnATIWPCtOUs506W05u7_z-H6lyZcctDzEJxOflW9IY79bExB4jkuCrSUBL7bAerB7lUEpI3ahWm1jlES7bd6n9ydyrG1X5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd3300290.mp4?token=t-ejjACXnsSyyHKDCyEncZAqgYUe2ycHUL4cygvXQ7p2S6LvvFQsT-sOfvE2Ea78-B8yaxXP2yCrJsb8eRrjAVtYu6iIodxCLWW2y5Qoi5Z6buknOOuRUnzWD18iKspLoDF6lz2RH7gZWa5t6VuoufavU2xRjgZ3XaRfChf2Ajzg9XE10kP6oqtwgjPx7Sn2Bfbo1urtexxhDJnW0bPLLFA1ASPSPRSrvnq8n24_K9wqyOiitZ5x2VnATIWPCtOUs506W05u7_z-H6lyZcctDzEJxOflW9IY79bExB4jkuCrSUBL7bAerB7lUEpI3ahWm1jlES7bd6n9ydyrG1X5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زین واکر بازیگر ایرانی هالیوود با انتشار این ویدیو از جمهوری اسلامی حمایت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148185" target="_blank">📅 15:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148184">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
امام جمعه دزفول: دختری که تا پاسی از شب در کافی‌شاپ‌ها و فروشگاه‌ها حضور دارد، نه فرزند خوب نه مادر مناسب و نه همسر موفقی خواهد بود.
🔴
پ.ن: این یکیو راست میگن
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148184" target="_blank">📅 15:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148183">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
معاون پزشکیان: شرایط اقتصادی خوب نیست؛ مجبوریم پول چاپ کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148183" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148182">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
دود از شهر ریاض در عربستان سعودی به هوا برده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148182" target="_blank">📅 14:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148181">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d0c461c6.mp4?token=YYe7CAtB3cUYkzlFAJa-nGRpqpV1hsDiB2E2xGqSXRR9wA0M-RTMSUKUUlXyox6uJo6NSDaO85heRonzlAw3MUpAZPVMHb_p5Yt-AS29_zuyywjdXqmkpnqm6xoSmqKb1iaJYQL_pDOKElFRGBm3yZiNQU58lIeMXW0gpKFXjJVy96Yj53rYnLPgl048gDGy0ByFZ0j3IzPPS-KDI3GOUKZRyAl4GlQ4OBQgWht5WAhudF0g_7ftKT1JOgLEunQX1xNjNQ0x87gS-ZLjn8g_nq3mhc0cqYI6Uz7OzQnPA58p_JD4B_59cJO_wldwpphUKOWPodbx3XrYd4mFC09vLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d0c461c6.mp4?token=YYe7CAtB3cUYkzlFAJa-nGRpqpV1hsDiB2E2xGqSXRR9wA0M-RTMSUKUUlXyox6uJo6NSDaO85heRonzlAw3MUpAZPVMHb_p5Yt-AS29_zuyywjdXqmkpnqm6xoSmqKb1iaJYQL_pDOKElFRGBm3yZiNQU58lIeMXW0gpKFXjJVy96Yj53rYnLPgl048gDGy0ByFZ0j3IzPPS-KDI3GOUKZRyAl4GlQ4OBQgWht5WAhudF0g_7ftKT1JOgLEunQX1xNjNQ0x87gS-ZLjn8g_nq3mhc0cqYI6Uz7OzQnPA58p_JD4B_59cJO_wldwpphUKOWPodbx3XrYd4mFC09vLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود از شهر ریاض در عربستان سعودی به هوا برده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148181" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148180">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مکرون دیروز  صبح تمام سران سیاسی فرانسه (حتی احزاب مخالف) را به جلسه‌ای محرمانه دعوت کرده بود. موضوع جلسه امنیت اروپا، احتمال گسترش جنگ در اروپا و خاورمیانه بوده است. جلساتی مشابه در آلمان و لهستان هم برگزار شده بود. گویا احتمال وقوع جنگ بین کشورهای اروپای…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148180" target="_blank">📅 14:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148179">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رسانه‌های عربی: پروازهای فرودگاه ملک خالد ریاض پس‌از اصابت پهپاد یمنی متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148179" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148178">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27b34a2bb.mp4?token=aH0ZhN4bqfn_IxdGnUTLTOZFn91jZzhX2dRsLZteuOGfLwXPQBBGjuY_PFPRaopzCxQ0ebaWVwy5_23237kcc6-JlZW4qTuSlxRNrVtxsHDXqPapAhhFlDGa5wOhxRpINYihMGXcgsEAOOmt3DPXK_EU-jz3AMB0hpLzRJum17uwNc-H9ftT7aG7fIkq_mUPtl2UnfvC_pGMy1hqT3pOt2_tNSYdxjzAfxH0XmiPGcecivHOKOG_g9PI65i3_waFrr2hiBPwGwCzebXCjthc-8XR4DIwUYITnpoV7UmvF8sNUo5w25rhYK66boQN8Qp4v4_GcfcTwnMjAevl1T0XNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27b34a2bb.mp4?token=aH0ZhN4bqfn_IxdGnUTLTOZFn91jZzhX2dRsLZteuOGfLwXPQBBGjuY_PFPRaopzCxQ0ebaWVwy5_23237kcc6-JlZW4qTuSlxRNrVtxsHDXqPapAhhFlDGa5wOhxRpINYihMGXcgsEAOOmt3DPXK_EU-jz3AMB0hpLzRJum17uwNc-H9ftT7aG7fIkq_mUPtl2UnfvC_pGMy1hqT3pOt2_tNSYdxjzAfxH0XmiPGcecivHOKOG_g9PI65i3_waFrr2hiBPwGwCzebXCjthc-8XR4DIwUYITnpoV7UmvF8sNUo5w25rhYK66boQN8Qp4v4_GcfcTwnMjAevl1T0XNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امام جمعه دزفول: دختری که تا پاسی از شب در کافه‌ها وقت می‌گذراند نه می‌تواند مادر خوبی باشد و نه همسر خوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148178" target="_blank">📅 14:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148177">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4n7eVKqJH2J2LK5WbxYZ40EnUjjJsEj52BPr-3ahZ4RiQ-kGu7j-Akb7CeNWKg_8ayCBvkyDvM64QGbXKRgSETcO1xh8rH5vo5k02D6crInlje06yNouA8ETk35XVFm7vaRZRQWfNXvoINMqywpyOQk8oA-U-ELZ2jvNFlrYy9AzUI-0yw_pXeHS7GvwhXMHAPiUHxWSanLa4XWdLwiRhhAkOga7F5UAAO1ijrEAY3DWfxHHHDs9AAPSzn0ZhuKTWHWz1aLe59gXPre6o6xUITnPqMr6yrvU4jTyojeUz35xyofH0rCnSve0mk-Z3XzrD1SQBnN5CAcnx8fq8hCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه‌های عربستان سعودی با مشکلاتی روبرو هستند...
🔴
تقریباً ۹ فروند هواپیمای مسافربری قادر به فرود در فرودگاه ملک خالد در پایتخت عربستان، ریاض، نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148177" target="_blank">📅 14:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148176">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رویترز: شعله‌های آتش و ستون بزرگی از دود سیاه در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148176" target="_blank">📅 14:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148175">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان به همتای ایرانی خود:ما بر لزوم تضمین عبور ایمن کشتی‌ها تأکید می‌کنیم، زیرا این امر به نفع زنجیره‌های تأمین انرژی جهانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148175" target="_blank">📅 14:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148174">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bcf4947eb.mp4?token=WVUZiAwUtUI7hf5TMqL1Mb8p4mgpq9xLlbb_pS3Awl3BfTj7wxVFmxfRNws184N-6sBJHvjCC1IcYgsBHO88EwMz7TTAswEn2Kcv8b9oR9B3lA8eePdYeVSuW71ArsecNtJLlvk82G-gepn9VdU-uY9rbJeNDJnbQYjw5zfFi4hk0UXpd4f7_ISXzAsmkZatP2nv0jpKxGIkx2ssoHLv7tDMOzMT4rf2lLS3wePvEPrlDGb3LP1muu9zdOQXls1MxrcH_d3D7VjF3FA7eHeJT5j6qGnqBMqz_8ty1QHqAEY_MA3kLygf6aUFo9PuDfW6eva_tzIGhDOlivyH2Uszrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bcf4947eb.mp4?token=WVUZiAwUtUI7hf5TMqL1Mb8p4mgpq9xLlbb_pS3Awl3BfTj7wxVFmxfRNws184N-6sBJHvjCC1IcYgsBHO88EwMz7TTAswEn2Kcv8b9oR9B3lA8eePdYeVSuW71ArsecNtJLlvk82G-gepn9VdU-uY9rbJeNDJnbQYjw5zfFi4hk0UXpd4f7_ISXzAsmkZatP2nv0jpKxGIkx2ssoHLv7tDMOzMT4rf2lLS3wePvEPrlDGb3LP1muu9zdOQXls1MxrcH_d3D7VjF3FA7eHeJT5j6qGnqBMqz_8ty1QHqAEY_MA3kLygf6aUFo9PuDfW6eva_tzIGhDOlivyH2Uszrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو صدا و سیما مجریا‌ با تراکتور اومدن وسط برنامه میگن با همین میخواییم اسرائیل رو شخم بزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148174" target="_blank">📅 13:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزارت دفاع روسیه:«ما یک نفتکش در بندر اودسا و یک کشتی باری در دریای سیاه را که برای پشتیبانی از نیروهای مسلح اوکراین مورد استفاده قرار می‌گرفتند، هدف قرار دادیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148173" target="_blank">📅 13:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
مذاکرات پکن و آمریکا در حوزه انرژی /  بازگشت چین به بازار LNG در بسته ۳۰ میلیارد دلاری
🔴
آمریکا و چین برای کاهش یا حذف تعرفه ۱۵ درصدی پکن بر گاز طبیعی مایع آمریکا مذاکره می‌کنند؛ توافقی که می‌تواند هم‌زمان با سفر رئیس‌جمهور چین به واشنگتن و در قالب بسته گسترده‌تری از قرارداد‌های انرژی و کشاورزی اعلام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148172" target="_blank">📅 13:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZHKTOdDw_0X0_remkeBjrr1pMZVY9Rj4dkKmE4vimW0u0Huh589-zOQWJg8bKxX5IIoJJIrE8NBGoTZG4SKnj1wI5gfgD_oE5Cs8HWcvC6vHhpsbmFhN_fz2sOZcsyDOQ1zZgMwBdVpMSc-zjMzg59zRb15sH37lcpzH0zf2sE7ovf1NV95X4c6kIw66SVh8WS6i86gjx3O4iCQKP7v1rxhe_7U-uoKPn_b_U7wYVOwyMVGF_4UYj4UhvxYHt2U9ea_tpf8ajNTSZvzrrzfFzTflte0Ev3-6Zbb-c9Ki465KHXcNphCGUe39IdRYwEXOzdvv4WtiPyqvazUf9KBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ ایران به پیشنهاد جدید آمریکا احتمالا منفی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148171" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سخنگوی ناتو: از اعلام توافق بین ایالات متحده، گرینلند و دانمارک استقبال می‌کنیم. این توافق، امنیت و ثبات در اقیانوس اطلس شمالی را تقویت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148170" target="_blank">📅 13:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148169">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ان بی‌سی: روبیو، وزیر خارجه آمریکا برخلاف ونس، از قرار گرفتن در کانون توجهات درباره جنگ نامحبوب ایران اجتناب کرده؛ این فاصله ممکن است از نظر سیاسی به سود او باشد
🔴
روبیو در تمام مدت این جنگ، یک «دست پنهان» بوده؛ او به تدوین راهبرد دولت ترامپ کمک کرده
🔴
به گفته افراد نزدیک به وی، نامزدی احتمالی او برای ریاست‌جمهوری می‌تواند روی میز باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148169" target="_blank">📅 13:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148168">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل: محور سخنرانی ترامپ در نشست سالانه مجمع عمومی سازمان ملل در هفته آینده، ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/148168" target="_blank">📅 13:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b3ec86ff.mp4?token=Ds58dXSaPf9vHC2wGTDlUNF0dkDavZ_A6rlnVs0teMntP2NXEgGs3_CgGSvqbziVAuoEvCSQJEGkngnuqbmXwlNZrSBMN3Y5IwkVKz_fqCoxKWOEfrfrjkaUeAfzhtLEOqPhQXoNUPGT3yjzCEk76Q8E09kzRxJeiCDZzu41JYr_o2s30wvq3llI1ld4A1EhyRQ_GAyomBSqrVEaEERXw9PbK_pjUJ0-191Y1us6RsBKUmZ-b011gpDnzVWD6PxGhFI6O-TjU1JuJ8Gkfo3o02ALh724jQGHCKmnr-SontZoIl8XJ1t3_ABQSnVVG9NbhlTLqRaxApj5GIBWs_3__A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b3ec86ff.mp4?token=Ds58dXSaPf9vHC2wGTDlUNF0dkDavZ_A6rlnVs0teMntP2NXEgGs3_CgGSvqbziVAuoEvCSQJEGkngnuqbmXwlNZrSBMN3Y5IwkVKz_fqCoxKWOEfrfrjkaUeAfzhtLEOqPhQXoNUPGT3yjzCEk76Q8E09kzRxJeiCDZzu41JYr_o2s30wvq3llI1ld4A1EhyRQ_GAyomBSqrVEaEERXw9PbK_pjUJ0-191Y1us6RsBKUmZ-b011gpDnzVWD6PxGhFI6O-TjU1JuJ8Gkfo3o02ALh724jQGHCKmnr-SontZoIl8XJ1t3_ABQSnVVG9NbhlTLqRaxApj5GIBWs_3__A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر پزشکیان: من هم جان‌فدای ایران هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/148167" target="_blank">📅 13:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148166">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_KWvp9YsCErzJDf-r8wpjUvT9kG3FDsfKjY0QS5cVvqv4TUi1CdDcTS1BM_J7-5g5anqeeecNX-q_UV6Tm0uutJR2h-Iz7yQtA3a-YZqRst6rxwMphXWK4OOzbfQmZ3YMg__2XG0lGmowQLdQDRYSrWT_GHlevbBZaGj5y0lfLLbsBltf_lRig16-ZMALiU9qp7AieuWZeRbBYR7TYdB-quuYmZ5JE9633spNt_xs1QG7n1Yz9hEhY5xE1WpFuun1UXKC-Fwy3WbqnR4qt824MuZAczxS-tmcErthBqaXncIG3KPd6zhJfWu0-bsTIwurifcVZDssme6GZNMnNXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه‌های عربستان سعودی با مشکلاتی روبرو هستند...
🔴
تقریباً ۹ فروند هواپیمای مسافربری قادر به فرود در فرودگاه ملک خالد در پایتخت عربستان، ریاض، نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148166" target="_blank">📅 12:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148165">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
النشره: حزب‌الله برای سناریوی شکست مذاکرات ایران و آمریکا آماده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148165" target="_blank">📅 12:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148164">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY__8TtGRkaXVF0jEU711p_m6HjeVc_bKFfkH5aGENTcj9a29f7uN3S_8TiWB69I6irYUxJVGyYJJEkxqoH_pCZRX6Ftejam4-pI9538cZQcZGw_o5ljdFAykj-FuO-FlwrRBKNwkYKqfm4JV_K2Y41huA8KR4OnQEuZVYsiSAE69kt5RE0MoHFtadK2qHdceOcRsjF61V9g7Xr8RmYp9Elzy3toO9T2MkX0r8d28a1hi4SWZpsFMZMlel_1qRPuOzzsGI0BEIHJny_ThinXPssJtiBj_r4PtWDjYjo7teUTJIlcqyC2FKTX1t0oTlUHarIwP-FTGruvRU4u5i5GeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پر بازدید از یک جانفدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/148164" target="_blank">📅 12:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148163">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148163" target="_blank">📅 12:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148162">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
هواشناسی: بارش پاییزی هم خشکسالی تهران را جبران نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148162" target="_blank">📅 12:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148161">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnNB2Jhm-fik6u7Nl0h51g0e2JEoSXmQvsyb1Q2WUVoLwsMxKKkN0sw4iqx0BtTiqNU18QmFioaDU9cCOHt6-NUIC5Ipt_nSK2Ohy_VMSETW5qhZ7Uj2lvECAOjx4G93t3jCc2LjZOVjvgqK1WPktJW7SKOVQzK9kUxB5DIqGXdbZduUSRV-_yAEvakSlssBjre9R_Jm4YSCKLE7HDlJQmPtC2PBansY7ScKnemxSkjOPyjyeViw13p5JOhIHa7seMf2td9LrxggDptCoYnrt-InX8JQCbp2ZT7FVyODjhDUh1K5vsDz6BOr1mJ_lEWxv9hRACKCMtSsmCYDWHWe9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مکرون دیروز  صبح تمام سران سیاسی فرانسه (حتی احزاب مخالف) را به جلسه‌ای محرمانه دعوت کرده بود. موضوع جلسه امنیت اروپا، احتمال گسترش جنگ در اروپا و خاورمیانه بوده است. جلساتی مشابه در آلمان و لهستان هم برگزار شده بود. گویا احتمال وقوع جنگ بین کشورهای اروپای غربی و روسیه بالاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148161" target="_blank">📅 12:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148160">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
جبهه اصلاحات: رأی مردم باید بر سیاست‌ها و جهت‌گیری کشور اثر بگذارد
🔴
جواد امام، سخنگوی جبهه اصلاحات ایران، با تأکید بر شایسته‌سالاری و اصلاح شیوه حکمرانی گفت انتخابات زمانی معنای واقعی دارد که رأی مردم بر سیاست‌ها، اولویت‌ها و جهت‌گیری عمومی کشور اثرگذار باشد و تنها به جابه‌جایی افراد در مناصب محدود نشود.
🔴
او با انتقاد از آنچه «بازار مشترک قدرت» خواند، گفت حضور مدیران در دولت‌های مختلف به‌خودی‌خود ایرادی ندارد و تجربه، تخصص و کارآمدی می‌تواند ادامه مسئولیت آنها را توجیه کند؛ اما روابط سیاسی، قومی، خانوادگی یا حلقه‌های قدرت نباید جایگزین شایستگی شود.
🔴
امام همچنین بر تفکیک مناصب سیاسی از بدنه کارشناسی تأکید کرد و کنار گذاشتن نیروهای متخصص با تغییر دولت‌ها را آسیب‌زا دانست.
🔴
به گفته او، حکمرانی سالم باید بر رأی مردم، شایستگی مدیران، حفظ تخصص در نظام اداری و تعیین مرز روشن میان سیاست و اداره کشور استوار باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148160" target="_blank">📅 12:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148159">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d462dd9ba9.mp4?token=gY0ShplykAQRutx9pEn4vAMwe6cIoUrpiW830GeoblmQXFZSbfsorN4eruWUwmUMLbjFCbDLrylnsVuhXzlFkLuVTMl_0gUsS3oC2TI0s9tGKYge74Q18PUz0-MdC3qiUvNXhnQ8iZVoG2E5gP1O5-XC7VDrS-_T28VUW93cjfI9VfPsmtaRf1OJ1dGAj6OCLFzrNaNuikrA53gCB03Vvxuc8OLBWn1yyB9JCGNqyYGjq5ywjIrvFfyvVt-F_o8HsrCpFOePFR-rl4WPUx-3ivVTN9A8gIzWrJrUnZtrkidM1CWccEZRmFxP770vHx_ZbQEfXUES7maZL_-QZG5vHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d462dd9ba9.mp4?token=gY0ShplykAQRutx9pEn4vAMwe6cIoUrpiW830GeoblmQXFZSbfsorN4eruWUwmUMLbjFCbDLrylnsVuhXzlFkLuVTMl_0gUsS3oC2TI0s9tGKYge74Q18PUz0-MdC3qiUvNXhnQ8iZVoG2E5gP1O5-XC7VDrS-_T28VUW93cjfI9VfPsmtaRf1OJ1dGAj6OCLFzrNaNuikrA53gCB03Vvxuc8OLBWn1yyB9JCGNqyYGjq5ywjIrvFfyvVt-F_o8HsrCpFOePFR-rl4WPUx-3ivVTN9A8gIzWrJrUnZtrkidM1CWccEZRmFxP770vHx_ZbQEfXUES7maZL_-QZG5vHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد بدون سرنشین سعودی در حال پرواز بر فراز استان صعده در یمن است و شهروندان محلی تلاش می‌کنند با سلاح‌های سبک آن را سرنگون کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148159" target="_blank">📅 12:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148158">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
گفتگوی تلفنی عراقچی و وزیر خارجه پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148158" target="_blank">📅 12:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148157">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa0bfc25e.mp4?token=k6twz1crtKKINDUiltInpXhTe4AZi4bB6oBjEOF2B3oRVej1oVJT6FGRWy8zgNjMn65FFjqBAISxTF-QyieUt7sYCPIwevx34rcWHiBqLmpulit9V0wRLnqbxNlECmYsTu1iI3cMNv8JBE1wy1p54FpOpfd6_jp6ovYRm4F02jrLAl_RsqEy4Cv0pTK0KECOyJOKinjWcq6cHt8Adl8UDB-RjfQ9qf2mQvuYh2mbjOjHsRhcjFT49zmKxKh1MAgYdM_fhs0o7n3RXLyotFOApEYf9_DBd7P-ewWGwV4AsBp3rVUhPgZd4XyxYRTj2ZSUVnOBK8nn1DiukBESeGgZdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa0bfc25e.mp4?token=k6twz1crtKKINDUiltInpXhTe4AZi4bB6oBjEOF2B3oRVej1oVJT6FGRWy8zgNjMn65FFjqBAISxTF-QyieUt7sYCPIwevx34rcWHiBqLmpulit9V0wRLnqbxNlECmYsTu1iI3cMNv8JBE1wy1p54FpOpfd6_jp6ovYRm4F02jrLAl_RsqEy4Cv0pTK0KECOyJOKinjWcq6cHt8Adl8UDB-RjfQ9qf2mQvuYh2mbjOjHsRhcjFT49zmKxKh1MAgYdM_fhs0o7n3RXLyotFOApEYf9_DBd7P-ewWGwV4AsBp3rVUhPgZd4XyxYRTj2ZSUVnOBK8nn1DiukBESeGgZdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هرکس پلیس بکُشد باید اعـدام شود
🔴
ترامپ: "مدت کوتاهی پس از آغاز به کارم، یک فرمان اجرایی تاریخی امضا کردم که بر اساس آن، هر کسی که به جرم کشتن یک افسر پلیس محکوم شود باید با مجازات اعدام روبه‌رو شود؛ و سال گذشته، کشته های پلیس حین خدمت به پایین‌ترین سطح در ۸٠ سال گذشته رسید."
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148157" target="_blank">📅 12:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148156">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKV0MfvlFYqBbm_kauokdRNXCAaihPhcIIgU_FH_A72Pg33Bwj4asj0c-UYKLfOYRQfLMmAN0T_kJ8txGTrnbF8XPRq6IZdQmgglipwDWvOJE21OJ60iKtal8S2H2muyrFOeH98sVKSCTvBwmjiMNnj7sc_5fkFt3C1AEWOoSO6KSzXCM8PjuXZxkL7aq9glgcZRF8xgSkui9wOti3OIvEjEB1cxxL3pMCbkR8c8x7Uqdwq-1_KQHoGr3HnCX7bAB3v7u9eSIIJ9Slq9FGQrMm81q5pYQ3KFR2juHoWQPVyBlYLiLwf4wPZzGyDu_HS9tiSd0WUKE-vx6auY9J_eIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعدادی از هواپیماهای مسافربری که قصد فرود در فرودگاه جده در عربستان سعودی را داشتند، به دلیل احتمال وقوع حمله، قادر به فرود در این فرودگاه نبودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148156" target="_blank">📅 12:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دادستانی تهران علیه عوامل برگزاری «دو مارتن تهران» اعلام جرم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148155" target="_blank">📅 11:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148154">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزیر خارجه کره‌جنوبی در دیدار با وزیر خارجه آمریکا، از آمادگی کشورش برای ارائه سهم قابل‌ توجه در تلاش‌ها برای بازگرداندن آزادی کشتیرانی در تنگه هرمز خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148154" target="_blank">📅 11:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148153">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پیمان اکبری مجری صدا سیما : به تجمعات عادت کنید، دیگه هم شب میاییم هم صبح
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148153" target="_blank">📅 11:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148152">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
شورای امنیت سازمان ملل حملات حوثی‌ها به عربستان سعودی، از جمله حملات علیه زیرساخت‌های غیرنظامی و انرژی را به‌شدت محکوم کرد و خواستار توقف فوری تشدید تنش‌های نظامی شد.
🔴
شورای امنیت همچنین تهدیدها علیه کشتیرانی در دریای سرخ و باب‌المندب را محکوم کرد، حق عربستان برای دفاع از خود بر اساس قوانین بین‌المللی را به رسمیت شناخت و بر تعهد خود به حاکمیت و تمامیت ارضی یمن تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148152" target="_blank">📅 11:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148151">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نیروی هوایی اوکراین اعلام کرد که در جریان حملات شبانه، ۱۴۱ پهپاد روسی را در مناطق مختلف این کشور سرنگون کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148151" target="_blank">📅 11:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148150">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
الجزیره: قانون جدید تحریم‌های ترامپ، اختیارات کلیدی تحریمی علیه ایران را تا سال ۲۰۳۱ حفظ می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148150" target="_blank">📅 11:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148149">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafde8acd9.mp4?token=i_twKrb9K3axuHYks0QGuXoPTWDQJSTtTSUt4rFnKpLrX8ZqwHvOoyYOwZKjHorM4-s0RRKMf7Ll_J6dFWJY8NnqSHMKeIzfrrl1JhM_dCmHtGID_fpWWGTyXvRgYaeTePDoMewFIBBkxArWEJ8ITeai4F0t4dOAf4Pjc5pM3NAlakdmcJFlu5XTcUsehJ9C6GGQU4_BYgFPrheyrhn-CmcXQ5DBQ0QgStp36COQZdKRxlcfxbpSX0LgMB6Vcso1ZHpkpKVNltzmRD_GrBCBdiGSvOjKP7tgFBCz2vTu3lQQqN0P7kF12T4aaix7jV-HUQX4LhkZ_Qy8y3UPQDIPjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafde8acd9.mp4?token=i_twKrb9K3axuHYks0QGuXoPTWDQJSTtTSUt4rFnKpLrX8ZqwHvOoyYOwZKjHorM4-s0RRKMf7Ll_J6dFWJY8NnqSHMKeIzfrrl1JhM_dCmHtGID_fpWWGTyXvRgYaeTePDoMewFIBBkxArWEJ8ITeai4F0t4dOAf4Pjc5pM3NAlakdmcJFlu5XTcUsehJ9C6GGQU4_BYgFPrheyrhn-CmcXQ5DBQ0QgStp36COQZdKRxlcfxbpSX0LgMB6Vcso1ZHpkpKVNltzmRD_GrBCBdiGSvOjKP7tgFBCz2vTu3lQQqN0P7kF12T4aaix7jV-HUQX4LhkZ_Qy8y3UPQDIPjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
هم اکنون ، ویدئویی از آتش سوزی یک رستوران در خیابان دولت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148149" target="_blank">📅 11:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148148">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قیمت بیت کوین پس از افزایش نرخ بهره در ژاپن به بالای ۸۱ هزار دلار جهش کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148148" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148147">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شبکه خبری سی‌ان‌ان: یک گزارش اطلاعاتی نادرست که با کمک هوش مصنوعی تهیه شده بود، در جریان جنگ آمریکا علیه ایران، ارتش این کشور را تا آستانه یک عملیات علیه یک کشتی چینی در خاورمیانه پیش برد و خطر درگیری نظامی میان واشنگتن و پکن را افزایش داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148147" target="_blank">📅 10:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148146">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: ترامپ در سخنرانی خود در سازمان ملل، به موضوع جلوگیری از دستیابی ایران به سلاح هسته‌ای می‌پردازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/148146" target="_blank">📅 10:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148144">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUtZ75-ZLuBs0OpgZ9n-IW2qqr7ufqFHVv5LCS9oU6y2-8mCrSRdxH7J23nYin8kAalW3LlU4EOgcaDgHsUHyXinXjhgV30bbyyHcdAnhN_7YovKMRknNh1afFKzWB4G7DKdGYcKwFra7PFgXPauK3Wp9ZV_VdDuYWOY68AIzz-iYDMk9YlSnzRIgmW8aeHSA5dhOYShnn4rz0LfkQXsj3-OE9-xoCC_OMSm0BvzAQRgaNp43eMHgiNGgeIXFnvG0tyb7MoiJnGucv-jW6NytQ2wDc8WFW2Upg3lFZRyC9lEFNovjU1ac6OYflMQIZgcCJcXsGMqXeF4_m3vL7UimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e84c2629.mp4?token=Q5pXJGmOK8yr_Syg9fTAXHY-LmuNCfGLdd8ooxV8uTxEIdMurJtgdYxx5OnYE3gGA7ar64sZKOAQc_vz7T06fL0_zdEMy8LISsWgLPUR_2a2gNhcxK8j0s9Dkm3tAeQsaq12Isee7dH7dkCFCMpFf26XZuzRvlr4CAHne9L1MPgxgIQGdjHJflmiJ7vJusR8MYIPnqetKVNFoNa5bKONkuFNNsobBmi55dlPkf3nGv6mGLqqugYprjVe_H8t2BpOAWHVPZk_m9UfqjH9XcE2VEudN8FS7kdeBc6VgPm0-59CE2t5IoQ49h4TNi_0Alr33tBOZpMp8ta-Pyg1N06TY2Bd89hHCqzUOfI0MTeffzC1yvUcHRSX-cxy4pasQjarcr_KqcVJZ-uFOU18V9mQHDhHRkA8fEVyTNTZp0y5NBC_T0xSNVah7OuHW3L1NQYdM7gv-VSyF1SQjQdkQKBzis4lmJQhJZ6pxRNvyumMZK36PB0gTadoyEF4S_CZgJZZR0rlYdF525XOmAM9kfiZtjXzh-39JMFOTzmwTEqhyJ0pTSq1fSuFgd3MRdSVKwV8BQHLKD2p1zBOqm5M-8rgW7cP9GKkfBZNl1mylvVKuh3FUXt2MChtU14kHNC2gIV-iQLm7Rnp4MCOj8WmAAbbjWg_ENzS_atp7lwuna5VDG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e84c2629.mp4?token=Q5pXJGmOK8yr_Syg9fTAXHY-LmuNCfGLdd8ooxV8uTxEIdMurJtgdYxx5OnYE3gGA7ar64sZKOAQc_vz7T06fL0_zdEMy8LISsWgLPUR_2a2gNhcxK8j0s9Dkm3tAeQsaq12Isee7dH7dkCFCMpFf26XZuzRvlr4CAHne9L1MPgxgIQGdjHJflmiJ7vJusR8MYIPnqetKVNFoNa5bKONkuFNNsobBmi55dlPkf3nGv6mGLqqugYprjVe_H8t2BpOAWHVPZk_m9UfqjH9XcE2VEudN8FS7kdeBc6VgPm0-59CE2t5IoQ49h4TNi_0Alr33tBOZpMp8ta-Pyg1N06TY2Bd89hHCqzUOfI0MTeffzC1yvUcHRSX-cxy4pasQjarcr_KqcVJZ-uFOU18V9mQHDhHRkA8fEVyTNTZp0y5NBC_T0xSNVah7OuHW3L1NQYdM7gv-VSyF1SQjQdkQKBzis4lmJQhJZ6pxRNvyumMZK36PB0gTadoyEF4S_CZgJZZR0rlYdF525XOmAM9kfiZtjXzh-39JMFOTzmwTEqhyJ0pTSq1fSuFgd3MRdSVKwV8BQHLKD2p1zBOqm5M-8rgW7cP9GKkfBZNl1mylvVKuh3FUXt2MChtU14kHNC2gIV-iQLm7Rnp4MCOj8WmAAbbjWg_ENzS_atp7lwuna5VDG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از روز گذشته ظاهرا حملات نیروهای تحت‌الحمایه عربستان با پهپادهای سری نقم و عیبان (معادل شاهد-۱۳۶ ایرانی) به اهدافی در اطراف صنعا آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148144" target="_blank">📅 10:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148143">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مولوی عبدالحمید: اگه حکومت حرف مردمو گوش میداد شرایط اینجوری نمیشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/148143" target="_blank">📅 10:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148142">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
مقامات ارشد دولت ترامپ می‌گویند که رئیس‌جمهور در جریان نشست مجمع عمومی سازمان ملل در نیویورک، با بنیامین نتانیاهو، دیدار نخواهد کرد!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148142" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148141">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عضو دفتر سیاسی جنبش انصارالله: ملت یمن با هرگونه آتش‌بس یا کاهش تنش، تا زمانی که عربستان محاصره یمن را رفع نکند، موافقت نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148141" target="_blank">📅 10:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148140">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
الجزیره: نهاد ناظر بانک‌های ترکیه، مجوز فعالیت شعبه «بانک ملت ایران» در استانبول را لغو کرد
🔴
بر اساس اطلاعیه‌ای که در روزنامه رسمی منتشر شد، نهاد تنظیم‌گر و ناظر بانک‌های ترکیه، مجوز فعالیت شعبه بانک ملت ایران در استانبول را لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148140" target="_blank">📅 09:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148139">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: توافق با دانمارک و گرینلند «تاریخی» است و بر اساس آن، منافع امنیتی ما در قطب شمال به طور دائمی و بدون هیچ هزینه‌ای تضمین می‌شود
🔴
مارکو روبیو، وزیر امور خارجه آمریکا در مورد توافق با دانمارک و گریلند گفت: این توافق تاریخی، یک پیروزی بزرگ برای ایالات متحده و مردم آمریکا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148139" target="_blank">📅 09:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148138">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc3cc6058d.mp4?token=PoVDuKLF3pcvR_qWK2eSMDcWkC0UMXkgY_ImVQeijutX0EYAXDhfezhPCIvW9vw10ONMk5S7HhhdjroY8hI7oBwApn9wgPKo8bk6ARmI6RtXQPvG7_nz1DDmu5IsGOJOAkkqtJ-426PXl0cuiVCy-dw-zORcVKxopFmoERvB6VSih42On6CEF0wfyOR_TzyS0WAQFDhFlvPl3-P7uD1gULisK6sOFf0hOCM0NH7tMSQuUz7lLajZ2QfNHprEPzh__2PDcajPoDJGho88EXhXdi9NhwXkqt7j3ZnrK6JBBkM5aTXuQWkVuBFsc9xX9IDPWr0qfy_4FDMUpWf2M6MkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc3cc6058d.mp4?token=PoVDuKLF3pcvR_qWK2eSMDcWkC0UMXkgY_ImVQeijutX0EYAXDhfezhPCIvW9vw10ONMk5S7HhhdjroY8hI7oBwApn9wgPKo8bk6ARmI6RtXQPvG7_nz1DDmu5IsGOJOAkkqtJ-426PXl0cuiVCy-dw-zORcVKxopFmoERvB6VSih42On6CEF0wfyOR_TzyS0WAQFDhFlvPl3-P7uD1gULisK6sOFf0hOCM0NH7tMSQuUz7lLajZ2QfNHprEPzh__2PDcajPoDJGho88EXhXdi9NhwXkqt7j3ZnrK6JBBkM5aTXuQWkVuBFsc9xX9IDPWr0qfy_4FDMUpWf2M6MkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: هفته آینده در سازمان ملل سخنرانی می‌کنید. پیام شما چیست؟
🔴
ترامپ: خب، سال گذشته اپراتور تله‌پرامپتر من را از ورود به سالن منع کردند. بنابراین من بدون تله‌پرامپتر آنجا ایستاده بودم. جالب نیست؟
🔴
خبرنگار : پیام شما چیست؟
🔴
ترامپ: یادتان هست؟ آن‌ها پله‌برقی را خاموش کردند.
🔴
خوشبختانه بانوی اول من خیلی محکم بود و من توانستم پشت او یا بخش دیگری از بدنش را بگیرم. در واقع، دستم کمی پایین‌تر از پشت او قرار گرفت و محکم گرفتمش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148138" target="_blank">📅 09:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148137">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
هزینه یک دست لاستیک ایرانی تا بیش از ۳۵ میلیون تومان رسید
🔴
آوش در گزارشی نوشته قیمت شش سایز پرمصرف لاستیک ایرانی اکنون بین ۴.۵ میلیون تا ۸ میلیون و ۷۵۰ هزار تومان برای هر حلقه قرار دارد.
🔴
بر این اساس، خرید یک دست چهارحلقه‌ای لاستیک برای بسیاری از خودروهای داخلی بین ۱۸ میلیون تا بیش از ۳۵ میلیون تومان هزینه دارد.
🔴
رقمی که نشان می‌دهد تعویض لاستیک، برای بخش بزرگی از رانندگان دیگر یک هزینه عادی نگهداری خودرو نیست و می‌تواند فشار قابل‌توجهی به بودجه خانوار وارد کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148137" target="_blank">📅 09:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148135">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWlwYjQC_swj1GkypFmvWZIUQHZp2swz8IMcHN_koSfCkT5ZsWG7OR5iNaacjMNBuvPVNUV4nWLmI-FYZjREiieprdHXIXNA_-dxl7rHeoOxMd5pdPe6_MsC3-2Wby3DGJxDhBPtBLwfx-hFzeJpPGzuN-xcd6-ejegUXZR63LIvmIb7eg7yUZn_EnXYpWrvygM931ocW-3K_AUBP9UgAJcHizIft1XxPVhkjUCgIYbTjIVKrdCBptyQOwysddLu3eCpXS7_1WwwN_KdKkyh_ZAEihCU9oV0-YGNmuSbgGgW6QbzEj9jPrSEt4WKCJTmcqg1hrqhVyBWf93K9t22nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLE7w_yWj_XB2OE0gabP2Y3DSoRENqVJUtnKh_rFbRjJB8pe1V6wraF5ZUfgmerKlsrhQBwTQZ5bicmpN2fKQPuyvKtKVEPzQrllJWVdX46nvP9Q7JfBVC71g_YUxcfSX7XYml56oPC7FHwqfz-V2P-cIZsC-Uqjc3YH8-NHpgdWFTfsScUkpOGtQLnTBocHeBpXD3aOnvb6zxCyFwI_d5P-p1WQ1nTS0QJDS8REpWKBTM_Z9Qpfa3mXa0_76GHnJTRDF_KUrKSaK70Ww-aG2JpB7DHUcXko8gNIXHi7w65AI7Y64OotWoP9iR5N2R6w3LXBDn3vDdM14Z1yWsRoTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا،
فهرست «
۲۵ دستاورد برتر ترامپ در دوره سوم
» را در شبکه اجتماعی
Truth Social
منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/148135" target="_blank">📅 09:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148134">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پروازهای هوایی در ریاض به دلیل موشک‌ها و پهپادهای حوثی ها متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148134" target="_blank">📅 09:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148133">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bB8MTteiJ7v-sLhZbGf3INWB-pQ-MT2hjb0o-_gtF9PNjSOuc5mf4PPSAsD9BXPzEwsutFMr9Ow0XeaPAkYzX2Ivx_YOKPhDFk8vJHvSmIzr4-sLhJggdpCOQ5Fp_ItPLC-tUTDoKN27eDxH057ooB0_cndju6wySLl8n3YWhTCG9Knkj76dOYeQmNzJlnxEhiP9q_EhTihPdxnemrWzuJTd561lNLIgP0jbw56eKlN923M5TpySoNOmtddcof8YJ1vSeaPCx1LCcQi-1nG0bWta12grQenRuSoBNAkqHxR-jhLW5O6ZNaTu-Wncb4-8VI_k3qobJz9vhMs1aK-4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر من، هدف حمله موشک بالستیک انصارالله به ریاض، احتمالاً پایگاه هوایی ملک سلمان در جنوب ریاض بوده است
🔴
اگر هدف پایگاه هوایی شاهزاده سلطان بود، احتمالاً هشدارهای اولیه برای ریاض صادر نمی‌شد؛ زیرا این پایگاه در فاصله حدود ۸۰ کیلومتری ریاض قرار دارد. همچنین در حمله ایران به پایگاه هوایی شاهزاده سلطان در اوایل سال جاری، معمولاً هشدارهای اولیه در ریاض فعال نمی‌شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/148133" target="_blank">📅 09:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148132">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
انتظار می‌رود شی جین پینگ، رئیس جمهور چین، هفته آینده در واشینگتن با دونالد ترامپ درباره آتش‌بس تجاری رو به پایان، معافیت میلیاردی تعرفه‌ها و هوش مصنوعی گفت‌وگو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148132" target="_blank">📅 08:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148131">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پنتاگون در تازه‌ترین برآورد خود اعتراف کرد جنگ با ایران تاکنون ۴۳.۶ میلیارد دلار برای آمریکا هزینه داشته است؛ رقمی که هنوز خسارت‌های واردشده به تأسیسات نظامی آمریکا در ۸ کشور غرب آسیا را شامل نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148131" target="_blank">📅 08:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148130">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxhPn8N7Etvf8ddc6GjPYJ9Vr5zP3Cnz3oVH9V91qYdaa9onWNaVdZq6JPeC3eLOLEHABRB-4Y1QgcG9EQOs21QxMsuvP6je3o3Q69ShDVZHZE51acsFhtgNBYskItBsatI23gf4spCGU1MDSkZmoZaWvyDqFhA7U1NIIBjQGz0B208KC894OV1uSh7-SvnCv1xvwhqz2985U5go50skN-RY0eur9yuoTvWHY6YvZJ8Bp7rUB6lTc2T7iKEryDcWaSAH4y5m9FhGkuNUOTEaIAhxBMj1Euc12rLJCFyfctRE1JtLwUm5H69bLjcsPr1Sgpe1lRxdREWcvlkI2HfSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا: شرم بر واشنگتن پست. این اطلاعات جعلی و دروغ است. آنها از رسانه دولتی ایران بدتر هستند.
‏
🔴
واشنگتن پست: بر ادعای خود باقی میمانیم. ۶ کشته بیش از آنچه اعلام کردید وجود دارد. واشنگتن پست اعلام کرده که تعداد کشته شدگان نظامی آمریکا در جنگ علیه ایران بیشتر از اعلام پنتاگون است
‏
🔴
به گفته ۶ مقام آمریکایی آشنا با داده‌های حسابداری تلفات داخلی وزارت جنگ، شمار نظامیان آمریکایی که در جنگ علیه ایران در کشته شده‌اند، بیشتر از آن است که پنتاگون اعلام کرده است.
‏
🔴
این مقامات تعداد کشته شدگان را دستکم  ۲۲ تا ۲۳ نفر اعلام کردند، پنتاگون در حال حاضر ۱۸ کشته را فهرست کرده است..
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/148130" target="_blank">📅 08:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148129">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: با دانمارک و گرینلند به توافقی دست یافته‌ایم که به آمریکا کنترل دائمی بر امنیت و نیازهای دیگر در گرینلند را می‌دهد
🔴
این توافق کاملا به همه نگرانی‌های متعدد واشنگتن رسیدگی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148129" target="_blank">📅 08:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148128">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEhQlJJDCHvvWdykA62XfTRJk6Pa69Go9OmWK_Mv5NPYfBA9xVh1LpMZWtgEpcF4z4zrS2Hej6hHbDyrOmQVlvmLofa84ozGtuNmNrw5L-HbYPavDeLIGQ9BbwcLs3wkeyirDOZEyvQs9rOzy38K1Xu_dxu6EB30dHJ3903t0ncqQdqGmPyejp_qyFPaWvojU2Q819PgCJ8eS5KoQQMbMNx4EWrmO_AnZd9OKbmp3P46EL6S0NzH_9CcWhPN534PzqOYwmtK0O_kTHCR7o9cnb1pGE-ySuv7W1qs1piCMIWkFx05es28Fdh9KSm1_U4mznr8ntm2Vh6iPqVADuJ34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه مجوز فعالیت شعبه بانک ملت در استانبول را لغو کرد!
🔴
نهاد ناظر بانکی ترکیه مجوز فعالیت شعبه استانبول بانک ملت، بانک کاملاً دولتی ایران، را لغو کرد
🔴
این نهاد دلیل تصمیم خود را «تهدید علیه ثبات نظام مالی» اعلام کرده است
🔴
شعبه بانک ملت از سال ۱۹۸۲ در ترکیه فعال بود، اما پس از تحریم‌های آمریکا عملاً از سوئیفت و سامانه انتقال بانکی EFT ترکیه کنار گذاشته شده بود.
🔴
لغو مجوز، پایان رسمی فعالیت این شعبه در ترکیه محسوب می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148128" target="_blank">📅 08:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148127">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) از کشته شدن ژنرال فرق العصار، فرمانده تیپ اول کماندویی، در نتیجه حمله هوایی عربستان سعودی در جبهه کهبوب در نزدیکی تنگه باب المندب خبر دادند.
🔴
گزارش‌ها حاکی از آن است که شش نفر از محافظان العصار نیز در این حمله کشته شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/148127" target="_blank">📅 08:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148126">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Arybd8mefZ2wlhbAvVu5G2OvI4Uviz9oFtB0JNYRyFnn4jB4Fxam-ftDEvg4gB0Z3qWzc5g8Vu6ncJJV_PWn0Gq3KthXBkZ5P-soJnL-kZ7EEXZTFJJlNrV1sXMnYGhTh74og6-0UorIOcgyJeCKl-0FmdhmY-bO9sOqTHjpW2J1PbL6C7XBY_eR-f8_uI17a0BXpqQz1nAUKIDowsjiMdgafHA64iucOiB4o4rpa3uc_-Vx7ZukHGOCW7wTXAAl8SRiiM8Taf-XsB5dCDL_cTvhXPmhjgp0xLgCSAkOP9IhVXI8saSH8wrVy516wrKZQeGd0TOgNdTiFQPCjD56-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای نظامی آمریکا به ABC News گفته‌اند که بیشتر پایگاه‌های نظامی آمریکا در خاورمیانه به‌طور غیرقابل‌جبرانی آسیب دیده‌اند و ترمیم آن‌ها ممکن است دهه‌ها طول بکشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/148126" target="_blank">📅 01:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148125">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، قانون «تحریم روسیه و ایران، لیندسی او. گراهام» در سال ۲۰۲۶ را امضا و آن را به قانون تبدیل کرد.
🔴
بر اساس این قانون، تحریم‌های قانونی، تعرفه‌ها و محدودیت‌های اعمال‌شده علیه روسیه گسترش می‌یابد و تحریم‌های موجود علیه ایران نیز…</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/148125" target="_blank">📅 01:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148124">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnDyJHl7PAn5NiKY2SxGlzqDIowbRcgRKBrufN4dSfGaW6_iZbAvWYXnvL62hKgyoAEh7fwk6IT9ARjnH5fFw74oE0vPscCxMt7tDfFZRdlLuSpBSf25wH3yTL4LYznuq2Fz994ZdCYD03gw9Alc9ZK6GA08WILtdQggqk-YRsZrP4rfy548o2Zuk8KzPhuKiO9_5P-SfJeWcCe14dyct60lOWzvhFvoS5wMxL9xZETNbQYY6ZlRA2_npUkpvmn4xUyUvSV1F2Ab_JCcHjB0qo32OewPy1GKxhbh5VlRRyQTz50laKwT_9lnJxjX6tnqgU4nsMbtEmuECX2bzHMygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا،
قانون «تحریم روسیه و ایران، لیندسی او. گراهام» در سال ۲۰۲۶
را امضا و آن را به قانون تبدیل کرد.
🔴
بر اساس این قانون،
تحریم‌های قانونی، تعرفه‌ها و محدودیت‌های اعمال‌شده علیه روسیه گسترش می‌یابد
و
تحریم‌های موجود علیه ایران نیز تمدید می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/148124" target="_blank">📅 01:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148123">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1eeaeb95.mp4?token=M1NEGuAQABU5iZdUNNwD8rgMzvLiatcSkDiX0bfVYkP8x435e9qtEVVQrVPjOTdmnffnqt0tjjcqyvrvVN4XScaHaQHcP_8COT_kmGVfpbo-NThxy2bTEkJTPmMvd15in6LrxNzuQLvQVsb2xxPDUacae6CdyAx3927y-M_RPfS4GAY4zNDlkPLn2OhZDYTpm-rtalAkQdWF8rlPnvMIqtqLJ8X2WUzGGTAhwOm1UE8VDcHAPoTmkq20FI7Ipw4F1LhngU7pvoAk5Zl1rzRNPnOImWA5Kl8w2sl8dPAj_n-02NJYr4k95DAb_RAGa0Y9jQ_bXk0m1dMgwHtR7GqIEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1eeaeb95.mp4?token=M1NEGuAQABU5iZdUNNwD8rgMzvLiatcSkDiX0bfVYkP8x435e9qtEVVQrVPjOTdmnffnqt0tjjcqyvrvVN4XScaHaQHcP_8COT_kmGVfpbo-NThxy2bTEkJTPmMvd15in6LrxNzuQLvQVsb2xxPDUacae6CdyAx3927y-M_RPfS4GAY4zNDlkPLn2OhZDYTpm-rtalAkQdWF8rlPnvMIqtqLJ8X2WUzGGTAhwOm1UE8VDcHAPoTmkq20FI7Ipw4F1LhngU7pvoAk5Zl1rzRNPnOImWA5Kl8w2sl8dPAj_n-02NJYr4k95DAb_RAGa0Y9jQ_bXk0m1dMgwHtR7GqIEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست:
«تنها رسانه‌ای که بهتر از ایران پروپاگاندای جعلی تولید می‌کند، رسانه‌های دچار جنون ترامپ در کشور خودمان هستند.
🔴
جدی می‌گویم. واقعاً تأسف‌بار است.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/148123" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148122">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پیت هگست : خسارات و تخریب‌هایی که ارتش ما به جمهوری اسلامی وارد کرده، بی‌سابقه بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/148122" target="_blank">📅 00:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148121">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ میگوید سازمان ملل متحد عمداً دستگاه پله برقی و دستگاه نمایش متن مورد استفاده او را در سخنرانی‌اش در مجمع عمومی سازمان ملل سال گذشته، از کار انداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/148121" target="_blank">📅 00:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148120">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYtaKYMdTicT0_kU4mF9oqWdEyznZwRZRR8MbX7wvh3SoN3NCXRJisQ2ZOrfQ4n3TxE0kKHBwBAdyCRKEicCS75H7L-dik2oK3Wsn9gUxmSBE3_SsxbeZv5g-HQXXKQcHQLotqTzRgWrR0mj5P2Uza24fqhRryke5Bk4QNsTT72ObA4B1P643mkqmID4e29hlzMTNP6xVG7Dq3PfPADJBGBtFSqzlsfZ-gRTcO71rLQlXQUfMc4czqME1us0bZZyrMVlWBaXF9-hVprjcSoZfHOfn2RF_M0r94UuOEUt5GQiB9i2dCdpAALJ283HGxJ81di6bt0NT1TPEp9p1Gj5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: ریشه تمام مشکلات بی حجابیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/148120" target="_blank">📅 00:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148119">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ : روزنامه نیویورک تایمز بسیار دروغگو است.
🔴
واشنگتن پست بسیار زننده است. من می‌گویم، آن‌ها زننده هستند.
🔴
من نمی‌فهمم. چرا باید این‌گونه باشند؟ ما بسیار خوب پیش می‌رویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/148119" target="_blank">📅 00:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148118">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
هشدار های در غرب عربستان سعودی دوباره فعال شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/148118" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
